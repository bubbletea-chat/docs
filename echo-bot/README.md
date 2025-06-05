# Echo Bot - BubbleTea Minimal Package Test

Simple echo bot to test the minimal BubbleTea Python SDK.

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the bot
python echo_bot.py

# 3. Test it
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"type": "user", "message": "Hello world!"}'
```

## 🤖 What it does

- Echoes your message back
- Shows basic message analysis 
- Displays images when requested

## 🧪 Testing

```bash
# Automated test
python test_bot.py

# Manual tests
curl -X POST "http://localhost:8000/chat" -H "Content-Type: application/json" -d '{"type": "user", "message": "show me an image"}'
curl -X POST "http://localhost:8000/chat" -H "Content-Type: application/json" -d '{"type": "user", "message": "hello echo bot"}'
```

## 📋 Example Response

```json
{
  "responses": [
    {"type": "text", "content": "🔄 Echo: Hello world!"},
    {"type": "markdown", "content": "## Message Analysis\n- **Words**: 2"},
  ]
}
```