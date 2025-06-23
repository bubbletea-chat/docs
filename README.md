# BubbleTea

[![Python 3.9+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-bubbletea.chat-purple.svg)](https://bubbletea.chat)

> Platform for Developers

**The Frontend Platform for AI Agents & Chatbots**

Share your AI creations with the world through beautiful, instant chat interfaces.

---

## Table of Contents

- [Overview](#overview)
- [How to Use](#how-to-use)
- [Types of Bots](#types-of-bots)
- [Developer Tools](#developer-tools)
- [Examples](#examples)

---

## Overview

### What is BubbleTea?

BubbleTea is a frontend platform that gives your AI agents and chatbots a home on the web. Think of it as the "user interface layer" for AI - where developers can instantly share their creations with the world through beautiful, accessible chat interfaces.

### 🎯 Core Purpose

- **Instant web interface for any AI bot** - Get a professional chat UI without writing frontend code
- **Share bots via simple URLs** - Each bot gets its own public URL at `bubbletea.chat/your-bot-name`
- **Unified chat experience for users** - Consistent, polished interface across all bots
- **Conversation history & user dashboard** - Users can access all their chats in one place

### 💡 Key Benefits

- **No frontend development needed** - Focus on your bot's logic, not UI code
- **Professional UI out of the box** - Mobile-friendly, accessible, and beautiful
- **Focus on AI logic, not UI code** - Build in any language, deploy anywhere
- **Built-in user management** - Authentication, sessions, and history handled for you

> **Note:** BubbleTea backend follows specific standards for bot integration. Check out the [Developer Tools](#developer-tools) section to learn about the API specifications and SDK.

### Bot Flow

Your bot connects to a foundational model, and probably contains some unique agentic functionality. It then connects to BubbleTea's API, which in turn, connects to a frontend.

### Who Benefits?

#### 🤖 For Bot Creators
Build your AI bot in any language, host it anywhere, and BubbleTea provides the chat interface

#### 🌍 For End Users
Access all your favorite AI bots in one place with a consistent, beautiful interface

#### 🛡️ Platform Benefits
Secure authentication, conversation history, and a unified dashboard for all interactions

---

## How to Use

### Getting Started with BubbleTea

Your journey from sign-up to sharing your first bot.

#### 1️⃣ Sign Up with Email
Enter your email address and we'll send you a verification code. No passwords needed!

[Sign Up Now →](https://bubbletea.chat/)

#### 2️⃣ Meet BT Agent - Your Bot Manager
BT Agent is your AI assistant for managing bots. Use natural language to register, list, and manage your bots.

Example commands:
- `"List all available bots"`
- `"Register my bot: weather-bot at http://myserver.com:8000/chat, streaming"`

#### 3️⃣ Get Your Public URL
Once registered, your bot gets a permanent public URL that you can share with anyone:

```
https://bubbletea.chat/your-bot-name
```

#### 4️⃣ Share & Track
Share your bot URL with users. All conversations are saved, and users can access their chat history from their personal dashboard. Your bot will appear in their bot list for easy access.

### Using BT Agent

BT Agent is your conversational interface for managing bots. Chat naturally to:

#### Common Commands
- `"List all bots"`
- `"Show my registered bots"`
- `"Register my bot: [bot-name] at [url], [streaming/non streaming]"`
- `"Update my bot settings"`

#### What Happens
- Bot gets registered to your account
- Receives public URL instantly
- Appears in user dashboards
- Conversations are tracked

[Chat with BT Agent →](https://bubbletea.chat/bt-agent)

---

## Types of Bots

### Types of Bots You Can Build

BubbleTea supports any type of AI bot - from simple chatbots to complex AI agents.

#### 💬 Conversational Assistants
Build Q&A bots, customer support agents, or personal assistants that can understand context and provide helpful responses.

**Examples:** FAQ bots, documentation assistants, language tutors

#### ✨ Creative AI Tools
Create bots that generate images, write stories, compose music, or help with creative projects.

**Examples:** Image generators, story writers, code assistants

#### ⚡ Task Automation Bots
Automate workflows, integrate with APIs, or perform complex multi-step tasks through conversation.

**Examples:** Data analysis bots, API integrators, workflow automators

#### 🌐 Specialized Domain Experts
Deploy bots with deep knowledge in specific fields like medicine, law, finance, or education.

**Examples:** Medical advisors, legal assistants, financial analysts

> **The best part?** You can build your bot in any language, using any framework. BubbleTea provides the chat interface so you can focus on your bot's unique capabilities.

### Bot Capabilities

#### What Your Bots Can Do
- Process text, images, and files
- Stream responses in real-time
- Maintain conversation context
- Integrate with external APIs

#### Rich Response Types
- Plain text and markdown
- Images and media
- Code blocks with syntax highlighting
- Custom UI components

---

## Developer Tools

### Tools for Building AI Bots & Agents

Everything you need to create bots that seamlessly integrate with BubbleTea's frontend.

These developer tools simplify the process of creating AI bots and agents that work perfectly with BubbleTea's chat interface. Build once, deploy anywhere, and let BubbleTea handle the user experience.

### 📦 Python SDK

Build powerful AI bots with our feature-rich Python SDK.

#### 🚀 Quick Start

```bash
# Install the SDK
pip install bubbletea-chat

# Create your first bot
from bubbletea_chat import bt

@bt.chatbot
async def my_bot(message: str):
    yield bt.Text(f"You said: {message}")

```
#### 🖥️ Server
```
if __name__ == "__main__":
    # Run the server
    bt.run_server(my_bot, port=8000)
```
- It will run the chatbot server on port 8000
    - Automatically creates a /chat endpoint for your bot

    - The /chat endpoint accepts POST requests with chat messages

    - Supports both streaming and non-streaming responses



## 🤖 LLM Integration

#### 🔧 Environment Variables

To use different LLM (Large Language Model) providers, set the appropriate API keys as environment variables:

```bash
# OpenAI
export OPENAI_API_KEY=your-openai-api-key

# Anthropic Claude
export ANTHROPIC_API_KEY=your-anthropic-api-key

# Google Gemini
export GEMINI_API_KEY=your-gemini-api-key
```

#### 🧠 Using the LLM Module
```python
from bubbletea_chat import LLM

# Use any LLM provider
# Make sure to set OPENAI_API_KEY environment variable
llm = LLM(model="gpt-4")
response = await llm.acomplete("Hello!")

# Stream responses
async for chunk in llm.stream("Tell me a story"):
    yield bt.Text(chunk)
```

#### 📸 Vision & Media Support

```python
# Analyze images
@bt.chatbot
async def vision_bot(message: str, images: list = None):
    if images:
        # Make sure to set OPENAI_API_KEY environment variable
        llm = LLM(model="gpt-4-vision-preview")
        response = await llm.acomplete_with_images(message, images)
        yield bt.Text(response)

# Generate images
image_url = await llm.agenerate_image("A sunset")
yield bt.Image(image_url)
```

> **Note:** The BT package automatically creates these endpoints for your bot:
> - `/chat` - Main bot endpoint for BubbleTea integration
> - `/docs` - Swagger API documentation
>
> When registering with BT Agent, provide your complete bot URL including the `/chat` endpoint (e.g., `https://my-bot-api.com/chat`).

### 🤖 BT Agent - Bot Management

Your AI assistant for registering and managing bots.

BT Agent is a built-in conversational interface that helps you manage your bots without writing code.

#### Common Commands
- `"Register my bot at http://localhost:8000/chat"`
- `"List all my bots"`
- `"Update bot description"`

#### Features
- Natural language commands
- Instant bot registration
- Bot discovery and search

[Try BT Agent →](https://bubbletea.chat/bt-agent)

### 📚 Developer Resources

#### Documentation
- [API Reference](#)
- [Tutorial Guide](#)
- [Best Practices](#)

#### Example Bots
- [Echo Bot](https://github.com/bubbletea/examples)
- [AI Assistant](https://github.com/bubbletea/examples)
- [Image Generator](https://github.com/bubbletea/examples)

[PyPI Package](https://pypi.org/project/bubbletea-chat/) | [GitHub](https://github.com/bubbletea)

---

## Examples

### Example Bots

Get inspired by these example implementations.

#### 🎨 Image Generation Bot
Generate images from text descriptions using DALL-E

```python
@bt.chatbot
async def art_bot(prompt: str):
    # Make sure to set OPENAI_API_KEY environment variable
    llm = LLM(model="dall-e-3")
    image_url = await llm.agenerate_image(prompt)
    yield bt.Image(image_url)
    yield bt.Text("Your image is ready!")
```

#### 📚 Knowledge Assistant
Answer questions using GPT-4 with streaming

```python
@bt.chatbot
async def assistant(message: str):
    # Make sure to set OPENAI_API_KEY environment variable
    llm = LLM(model="gpt-4")
    yield bt.Text("Let me help you with that...")
    
    async for chunk in llm.stream(message):
        yield bt.Text(chunk)
```

#### 👁️ Vision Analyzer
Analyze images and answer questions about them

```python
@bt.chatbot
async def vision_bot(message: str, images: list = None):
    if images:
        # Make sure to set OPENAI_API_KEY environment variable
        llm = LLM(model="gpt-4-vision-preview")
        analysis = await llm.acomplete_with_images(message, images)
        yield bt.Markdown(analysis)
```

[View More Examples →](https://github.com/bubbletea/examples)

---

## Ready to Build?

Join developers building the next generation of AI assistants.

[Get Started Free](https://bubbletea.chat/signup) | [Try BT Agent](https://bubbletea.chat/bt-agent)

---

Built with ❤️ by the Bubbletea team