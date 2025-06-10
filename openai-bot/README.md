# OpenAI GPT Bot Examples

Non-streaming bot examples using OpenAI's GPT models with BubbleTea.

## Features

This example demonstrates:
- Non-streaming responses (complete response at once)
- Multiple bot personalities (assistant, code helper, etc.)
- Using different GPT models (GPT-4, GPT-3.5-turbo)
- Returning multiple components
- Custom system prompts

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your OpenAI API key:
```bash
export OPENAI_API_KEY=your-api-key-here
```

Or create a `.env` file:
```
OPENAI_API_KEY=your-api-key-here
```

## Available Bots

### 1. GPT Assistant (`gpt_assistant`)
- Uses GPT-4 for high-quality responses
- General-purpose assistant
- Non-streaming mode

### 2. GPT Turbo Assistant (`gpt_turbo_assistant`)
- Uses GPT-3.5-turbo for faster responses
- Returns formatted markdown
- More cost-effective

### 3. Code Assistant (`code_assistant`)
- Specialized for programming questions
- Uses lower temperature for accuracy
- Formats code with markdown

### 4. Multi-Response Bot (`multi_response_bot`)
- Demonstrates multiple LLM calls
- Returns multiple components
- Shows summary + full response

## Running the Bots

Run the default GPT assistant:
```bash
python bots/openai_assistant.py
```

The bot will start on port 8005. Test it with:
```bash
curl -X POST "http://localhost:8005/chat" \
  -H "Content-Type: application/json" \
  -d '{"type": "user", "message": "What is Python?"}'
```

## Customization

To use a different bot, modify the last line in `openai_assistant.py`:
```python
# Change to any of these:
run_server(gpt_turbo_assistant, port=8005)
run_server(code_assistant, port=8005)
run_server(multi_response_bot, port=8005)
```

## Non-Streaming vs Streaming

These examples use `@chatbot(stream=False)` which means:
- The entire response is generated before sending
- Better for short responses or when you need the full content
- Useful when doing multiple LLM calls or post-processing

For streaming examples, see the main BubbleTea examples.