# Anthropic Claude Bot Examples

Non-streaming bot examples using Anthropic's Claude models with BubbleTea.

## Features

This example demonstrates:
- Non-streaming responses with Claude 3 models
- Different Claude variants (Opus, Sonnet, Haiku)
- Specialized assistants (researcher, writer, tutor, debate bot)
- Multi-perspective analysis
- Complex reasoning tasks

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your Anthropic API key:
```bash
export ANTHROPIC_API_KEY=your-api-key-here
```

Or create a `.env` file:
```
ANTHROPIC_API_KEY=your-api-key-here
```

## Available Bots

### 1. Claude Assistant (`claude_assistant`)
- Uses Claude 3 Opus for highest quality
- Best for complex reasoning
- Most capable model

### 2. Claude Sonnet Assistant (`claude_sonnet_assistant`)
- Uses Claude 3 Sonnet for balanced performance
- Good speed-to-quality ratio
- Recommended for most use cases

### 3. Claude Haiku Assistant (`claude_haiku_assistant`)
- Uses Claude 3 Haiku for speed
- Most cost-effective
- Great for simple queries

### 4. Claude Researcher (`claude_researcher`)
- Comprehensive analysis
- Multiple perspectives
- Systematic breakdowns

### 5. Claude Writer (`claude_writer`)
- Adaptive writing assistance
- Various content types
- Professional output

### 6. Claude Tutor (`claude_tutor`)
- Step-by-step explanations
- Practice questions
- Adaptive teaching

### 7. Claude Debate Bot (`claude_debate_bot`)
- Multiple viewpoints
- Pro/con analysis
- Critical thinking

## Running the Bots

Run the default Claude Sonnet assistant:
```bash
python bots/claude_assistant.py
```

The bot will start on port 8007. Test it with:
```bash
curl -X POST "http://localhost:8007/chat" \
  -H "Content-Type: application/json" \
  -d '{"type": "user", "message": "Explain the theory of relativity"}'
```

## Customization

To use a different bot, modify the last line in `claude_assistant.py`:
```python
# Change to any of these:
run_server(claude_assistant, port=8007)  # Opus
run_server(claude_haiku_assistant, port=8007)  # Haiku
run_server(claude_researcher, port=8007)
run_server(claude_writer, port=8007)
run_server(claude_tutor, port=8007)
run_server(claude_debate_bot, port=8007)
```

## Model Comparison

| Model | Speed | Quality | Cost | Best For |
|-------|-------|---------|------|----------|
| Opus | Slower | Highest | Higher | Complex reasoning, analysis |
| Sonnet | Medium | High | Medium | General use, balanced needs |
| Haiku | Fast | Good | Low | Quick responses, simple tasks |

## Use Cases

1. **Research**: Use the researcher bot for in-depth analysis
2. **Writing**: Use the writer bot for content creation
3. **Learning**: Use the tutor bot for educational content
4. **Analysis**: Use the debate bot for multiple perspectives
5. **General**: Use Sonnet for most everyday tasks

## Non-Streaming Advantages

These examples showcase when non-streaming is beneficial:
- Multiple LLM calls (debate bot)
- Post-processing responses (writer bot)
- Adding metadata and formatting
- Complete responses for analysis

## Tips

- Claude excels at nuanced, thoughtful responses
- Use lower temperatures for factual content
- Use higher temperatures for creative tasks
- Claude handles long contexts well