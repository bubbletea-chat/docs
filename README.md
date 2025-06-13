# BubbleTea Sample Bots

A collection of example bots demonstrating various features and integrations with the BubbleTea framework.

## Available Examples

### 🤖 LLM-Powered Bots (Non-Streaming)

These examples demonstrate how to use various LLM providers with BubbleTea in non-streaming mode:

#### 1. **OpenAI GPT Bots** (`openai-bot/`)
- Multiple GPT models (GPT-4, GPT-3.5-turbo)
- Specialized assistants (code helper, multi-response)
- Complete responses without streaming

#### 2. **Google Gemini Bots** (`gemini-bot/`)
- Gemini Pro and Flash models
- Specialized personalities (analyst, educator, creative)
- Educational content with visual aids

#### 3. **Anthropic Claude Bots** (`claude-bot/`)
- Claude 3 models (Opus, Sonnet, Haiku)
- Advanced assistants (researcher, writer, tutor, debate)
- Complex reasoning and multi-perspective analysis

### 📸 Vision/Multimodal Bots

#### **Vision Bot** (`vision-bot/`)
- Image analysis with GPT-4V, Claude 3, Gemini Vision
- Multiple specialized vision bots:
  - General vision assistant
  - Screenshot analyzer (with code generation)
  - Document reader (OCR)
  - Chart interpreter
  - Multi-image comparison
  - Accessibility checker
- Supports URL and base64 images

### 🔊 Basic Bot Example

#### **Echo Bot** (`echo-bot/`)
- Simple echo functionality
- Basic bot structure
- Good starting point for beginners

## Quick Start

1. **Choose a bot example** from the directories above
2. **Navigate to the bot directory**:
   ```bash
   cd openai-bot/  # or gemini-bot/, claude-bot/, echo-bot/
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up API keys** (for LLM bots):
   ```bash
   # For OpenAI
   export OPENAI_API_KEY=your-key-here
   
   # For Gemini
   export GEMINI_API_KEY=your-key-here
   
   # For Claude
   export ANTHROPIC_API_KEY=your-key-here
   ```
5. **Run the bot**:
   ```bash
   python bots/<bot_name>.py
   ```

## LLM Bot Comparison

| Provider | Models | Best For | Key Features |
|----------|--------|----------|--------------|
| OpenAI | GPT-4, GPT-3.5-turbo | General purpose, code | Wide ecosystem, function calling |
| Gemini | Pro, Flash, 1.5 | Speed, multimodal | Fast responses, vision capabilities |
| Claude | Opus, Sonnet, Haiku | Complex reasoning | Thoughtful responses, long context |

## Non-Streaming vs Streaming

The LLM examples use **non-streaming mode** (`@chatbot(stream=False)`), which means:

### Advantages:
- Complete response before display
- Can process/format the full response
- Multiple LLM calls in sequence
- Better for short responses

### When to Use:
- Analysis requiring full context
- Multi-step processing
- Adding metadata after generation
- Response post-processing

### Streaming Alternative:
For streaming examples, check the main BubbleTea package examples which demonstrate real-time token streaming.

## Creating Your Own Bot

Use these examples as templates:

1. **Basic Structure** - Start with echo-bot
2. **Add LLM** - Copy from any LLM example
3. **Customize** - Modify prompts and behavior
4. **Deploy** - Run locally or deploy to server

## Features Demonstrated

- ✅ Non-streaming LLM responses
- ✅ Multiple LLM providers (OpenAI, Gemini, Claude)
- ✅ Different model variants
- ✅ Specialized bot personalities
- ✅ Multi-component responses
- ✅ System prompts and context
- ✅ Vision/multimodal capabilities
- ✅ Image analysis (URL and base64)
- ✅ Error handling
- ✅ Environment variables

## Resources

- [BubbleTea Documentation](https://docs.bubbletea.dev)
- [LiteLLM Documentation](https://docs.litellm.ai)
- [API Key Setup Guides](#)

## Contributing

Feel free to add your own bot examples! Follow the existing structure:
```
your-bot/
├── README.md
├── requirements.txt
└── bots/
    └── your_bot.py
```

## License

These examples are provided under the MIT License.