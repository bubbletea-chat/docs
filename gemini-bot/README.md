# Google Gemini Bot Examples

Non-streaming bot examples using Google's Gemini models with BubbleTea.

## Features

This example demonstrates:
- Non-streaming responses with Gemini models
- Different Gemini model variants (Pro, Flash)
- Specialized bot personalities (analyst, educator, creative)
- Multi-component responses
- Integration with images for educational content

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your Google/Gemini API key:
```bash
export GEMINI_API_KEY=your-api-key-here
```

Or create a `.env` file:
```
GEMINI_API_KEY=your-api-key-here
```

## Available Bots

### 1. Gemini Assistant (`gemini_assistant`)
- Uses Gemini Pro for balanced performance
- General-purpose assistant
- Straightforward responses

### 2. Gemini Flash Assistant (`gemini_flash_assistant`)
- Uses Gemini 1.5 Flash for speed
- Optimized for quick responses
- Includes response metadata

### 3. Gemini Analyst (`gemini_analyst`)
- Analytical and structured responses
- Lower temperature for consistency
- Data-driven insights

### 4. Gemini Creative Bot (`gemini_creative_bot`)
- High temperature for creativity
- Generates multiple variations
- Perfect for brainstorming

### 5. Gemini Educator (`gemini_educator`)
- Educational explanations
- Examples and analogies
- Can include visual aids

## Running the Bots

Run the default Gemini assistant:
```bash
python bots/gemini_assistant.py
```

The bot will start on port 8006. Test it with:
```bash
curl -X POST "http://localhost:8006/chat" \
  -H "Content-Type: application/json" \
  -d '{"type": "user", "message": "Explain quantum computing"}'
```

## Customization

To use a different bot, modify the last line in `gemini_assistant.py`:
```python
# Change to any of these:
run_server(gemini_flash_assistant, port=8006)
run_server(gemini_analyst, port=8006)
run_server(gemini_creative_bot, port=8006)
run_server(gemini_educator, port=8006)
```

## Model Selection

Gemini offers different models for different use cases:
- **gemini-pro**: Balanced performance and quality
- **gemini-1.5-flash**: Optimized for speed
- **gemini-1.5-pro**: Coming soon, highest capability

## Tips

1. **For Analysis**: Use the analyst bot with specific questions
2. **For Learning**: Use the educator bot for explanations
3. **For Ideas**: Use the creative bot for brainstorming
4. **For Speed**: Use the Flash variant for quick responses

## Non-Streaming Benefits

These non-streaming examples are ideal for:
- Short to medium responses
- When you need the complete text for processing
- Multiple LLM calls in sequence
- Adding metadata or formatting after generation