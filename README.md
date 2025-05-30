# 🧋 Overview

BubbleTea provides a beautiful chatbot frontend interface. Developers can integrate their AI chatbot backends by implementing our simple API schema and get a professionally designed chatbot UI hosted on BubbleTea.

## 🚀 Documentation Features

### 📍 Navigation Sections
- **Integration Process** - Step-by-step guide to get started
- **API Schema** - Complete request/response reference
- **Streaming** - Real-time streaming implementation
- **Examples** - Working code in FastAPI, Express, Flask

## 🎯 Integration Process

1. **Build your API** - Implement the required schema in your framework
2. **Sign up at BubbleTea** - Create account and start onboarding on https://bubbletea.chat/bt
4. **Connect & deploy** - Provide your API URL to get dedicated chatbot UI


## 🔧 API Integration Requirements

### Request Format
All chatbot APIs must accept POST requests to your bot API url:

```json
{
  "messages": [
    {
      "role": "user", 
      "content": "Hello!"
    }
  ]
}
```

### Non-Streaming Response should be in the following format:

```json
{
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Hello! How can I help you today?"
      },
      "finish_reason": "stop"
    }
  ]
}
```

### Streaming Response
```
data: {"choices":[{"delta":{"content":"Hello"}, "finish_reason":null}}]}
data: {"choices":[{"delta":{"content":"! How"}, "finish_reason":null}}]}
data: {"choices":[{"delta":{"content":" can I help?"}, "finish_reason":null}}]}
data: [DONE]
```
## Examples

### Non-Streaming Bot Example (FastAPI)

```python
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]

@app.post("/chat/completions")
async def echo_chat(request: ChatRequest):
    content_text = request.messages[0].content

    formatted_response = {
        "choices": [{
            "index": 0,
            "message": {
                "role": "assistant",
                "content": f"Echo: {content_text}",
            },
            "finish_reason": "stop",
        }]
    }

    return JSONResponse(content=formatted_response)
```

### Streaming Bot Example  (FastAPI)
```python

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]

def fake_stream_response(content: str):
    # Simulates streaming response word by word
    async def generator():
        for word in content.split():
            yield f'data: {{"choices":[{{"delta":{{"content":"{word}"}}}}]}}\n'
    return generator()

@app.post("/chat/completions")
async def chat_completions(request: ChatRequest):
    user_input = request.messages[0].content
    return StreamingResponse(
        fake_stream_response(f"Echo: {user_input}"),
        media_type="text/event-stream",
    )

```