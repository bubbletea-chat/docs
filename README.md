# 🧋 Bubble Tea Bot Development Guide

Learn how to create AI chatbots compatible with the **Bubble Tea** platform using our component-based schema system.

## 🎯 Overview

Bubble Tea uses a simple, flexible component system that lets you build rich, interactive chatbot responses. Instead of plain text, you can send structured components like text, images, and markdown that render beautifully in the frontend.

## 📋 Component Types

### 1. Text Component
```json
{
  "type": "text",
  "content": "Hello! This is a text component."
}
```

### 2. Image Component  
```json
{
  "type": "image",
  "url": "https://example.com/image.jpg",
  "alt": "Optional alt text"
}
```

### 3. Markdown Component
```json
{
  "type": "markdown", 
  "content": "# Heading\n\n**Bold text** and `code`"
}
```

### 4. Done Component (Streaming Only)
```json
{
  "type": "done"
}
```

## 🔄 Request/Response Format

### Request Schema
All bot APIs must accept this request format:

```json
{
  "type": "user",
  "message": "User's message here"
}
```

### Response Schemas

#### Non-Streaming Response
```json
{
  "responses": [
    { "type": "text", "content": "Hello!" },
    { "type": "image", "url": "https://example.com/cat.jpg", "alt": "Cat" },
    { "type": "markdown", "content": "## Markdown\n\nWith **formatting**" }
  ]
}
```

#### Streaming Response (Server-Sent Events)
```
data: { "type": "text", "content": "Hello there!" }
data: { "type": "text", "content": "How are you?" }
data: { "type": "image", "url": "https://example.com/image.jpg" }
data: { "type": "done" }
```

## 🤖 Bot Examples

### Example 1: Simple Text Bot (Non-Streaming)

```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Literal

class ComponentChatRequest(BaseModel):
    type: Literal["user"]
    message: str

class TextComponent(BaseModel):
    type: Literal["text"]
    content: str

class ComponentChatResponse(BaseModel):
    responses: List[TextComponent]

app = FastAPI()

@app.post("/chat")
async def simple_text_bot(request: ComponentChatRequest):
    responses = [
        TextComponent(type="text", content=f"You said: {request.message}"),
        TextComponent(type="text", content="This is a simple text response!")
    ]
    return ComponentChatResponse(responses=responses)
```

### Example 2: Streaming Text Bot

```python
from fastapi.responses import StreamingResponse
import asyncio

class DoneComponent(BaseModel):
    type: Literal["done"]

@app.post("/chat")
async def streaming_text_bot(request: ComponentChatRequest):
    async def stream_response():

        # logic / llm calls

        for stream in your_stream:
            component = TextComponent(type="text", content=f"{stream} ")
            yield f"data: {component.json()}\n\n"
            await asyncio.sleep(0.5)
        
        # Send done signal
        done_component = DoneComponent(type="done")
        yield f"data: {done_component.json()}\n\n"
    
    return StreamingResponse(stream_response(), media_type="text/event-stream")
```

### Example 3: Mixed Content Bot (Non-Streaming)

```python
from typing import Union, Optional

class ImageComponent(BaseModel):
    type: Literal["image"]
    url: str
    alt: Optional[str] = None

class MarkdownComponent(BaseModel):
    type: Literal["markdown"]
    content: str

# Union type for mixed responses
Component = Union[TextComponent, ImageComponent, MarkdownComponent]

class ComponentChatResponse(BaseModel):
    responses: List[Component]

@app.post("/chat")
async def mixed_content_bot(request: ComponentChatRequest):
    responses = [
        TextComponent(
            type="text", 
            content="Here's a mixed content response!"
        ),
        ImageComponent(
            type="image",
            url="https://picsum.photos/400/300", 
            alt="Random image"
        ),
        MarkdownComponent(
            type="markdown",
            content=f"""
## Your Message
You said: **{request.message}**

### Features:
- ✅ Text components
- ✅ Image components  
- ✅ Markdown components

```python
# Example code block
def hello():
    return "world"
```""".strip()
        ),
        TextComponent(
            type="text",
            content="That's all! 🎉"
        )
    ]
    return ComponentChatResponse(responses=responses)
```

### Example 4: Streaming Mixed Content Bot

```python
@app.post("/chat")
async def streaming_mixed_bot(request: ComponentChatRequest):
    async def stream_response():
        # Send text
        text_component = TextComponent(type="text", content="Loading response...")
        yield f"data: {text_component.json()}\n\n"
        await asyncio.sleep(1)
        
        # Send image
        image_component = ImageComponent(
            type="image",
            url="https://picsum.photos/400/300",
            alt="Streamed image"
        )
        yield f"data: {image_component.json()}\n\n"
        await asyncio.sleep(1)
        
        # Send markdown
        markdown_component = MarkdownComponent(
            type="markdown",
            content=f"## Response\n\nYou asked: **{request.message}**"
        )
        yield f"data: {markdown_component.json()}\n\n"
        await asyncio.sleep(1)
        
        # Send final text
        final_text = TextComponent(type="text", content="Streaming complete!")
        yield f"data: {final_text.json()}\n\n"
        
        # Send done signal
        done_component = DoneComponent(type="done")
        yield f"data: {done_component.json()}\n\n"
    
    return StreamingResponse(stream_response(), media_type="text/event-stream")
```

## 🌐 Other Frameworks

### Express.js (Node.js)

```javascript
const express = require('express');
const app = express();

app.post('/chat', (req, res) => {
  const { message } = req.body;
  
  res.json({
    responses: [
      { type: 'text', content: `You said: ${message}` },
      { 
        type: 'image', 
        url: 'https://picsum.photos/400/300',
        alt: 'Random image'
      },
      {
        type: 'markdown',
        content: '## Hello from Express!\n\nThis is **markdown** content.'
      }
    ]
  });
});
```

## 🧪 Testing Your Bot

### 1. Test Non-Streaming Response
```bash
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"type": "user", "message": "Hello bot!"}'
```

### 2. Test Streaming Response
```bash
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -H "Accept: text/event-stream" \
  -d '{"type": "user", "message": "Stream me something!"}'
```

## 📝 Schema Validation

### Pydantic Models (Python)
```python
from pydantic import BaseModel
from typing import List, Optional, Union, Literal

class TextComponent(BaseModel):
    type: Literal["text"]
    content: str

class ImageComponent(BaseModel):
    type: Literal["image"]
    url: str
    alt: Optional[str] = None

class MarkdownComponent(BaseModel):
    type: Literal["markdown"]
    content: str

class DoneComponent(BaseModel):
    type: Literal["done"]

Component = Union[TextComponent, ImageComponent, MarkdownComponent, DoneComponent]

class ComponentChatRequest(BaseModel):
    type: Literal["user"]
    message: str

class ComponentChatResponse(BaseModel):
    responses: List[Component]
```

### TypeScript Types
```typescript
type TextComponent = {
  type: 'text';
  content: string;
};

type ImageComponent = {
  type: 'image';
  url: string;
  alt?: string;
};

type MarkdownComponent = {
  type: 'markdown';
  content: string;
};

type DoneComponent = {
  type: 'done';
};

type Component = TextComponent | ImageComponent | MarkdownComponent | DoneComponent;

type ChatRequest = {
  type: 'user';
  message: string;
};

type ChatResponse = {
  responses: Component[];
};
```

**Ready to build amazing chatbots?** Start with one of the examples above and customize it for your use case! 🧋
