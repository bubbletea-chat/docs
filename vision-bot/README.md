# Vision Bot Examples

Multimodal bot examples that can analyze images using vision-enabled LLMs with BubbleTea.

## Features

This example collection demonstrates:
- 📸 Image analysis with multiple vision models
- 🔄 Comparing multiple images
- 📄 OCR and document reading
- 📊 Chart and diagram interpretation
- 🖥️ Screenshot analysis and UI code generation
- ♿ Accessibility checking
- 🎨 Creative image interpretation

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your API keys for the vision models you want to use:
```bash
# For GPT-4 Vision
export OPENAI_API_KEY=your-openai-key

# For Claude 3 Vision
export ANTHROPIC_API_KEY=your-anthropic-key

# For Gemini Vision
export GEMINI_API_KEY=your-gemini-key
```

Or create a `.env` file:
```
OPENAI_API_KEY=your-openai-key
ANTHROPIC_API_KEY=your-anthropic-key
GEMINI_API_KEY=your-gemini-key
```

## Available Bots

### 1. Vision Assistant (`vision_assistant`)
General-purpose image analysis bot that can:
- Describe images in detail
- Answer questions about images
- Work with multiple images
- Handle both URLs and uploaded files

### 2. Screenshot Analyzer (`screenshot_analyzer`)
Specialized for UI/UX analysis:
- Identifies UI components
- Explains functionality
- Suggests improvements
- Generates code (React, HTML/CSS)

### 3. Document Reader (`document_reader`)
OCR and text extraction:
- Handwritten notes
- Forms and documents
- Receipts and invoices
- Multi-language support

### 4. Chart Interpreter (`chart_interpreter`)
Data visualization analysis:
- Bar charts, line graphs, pie charts
- Flowcharts and diagrams
- Technical drawings
- Extracts insights and trends

### 5. Multi-Image Compare (`multi_image_compare`)
Compares multiple images:
- Before/after analysis
- Product comparisons
- Design variations
- Spot differences

### 6. Creative Interpreter (`creative_interpreter`)
Artistic and creative analysis:
- Art style analysis
- Story generation
- Mood detection
- Poetry creation

### 7. Accessibility Checker (`accessibility_checker`)
Checks for accessibility issues:
- Color contrast
- Text readability
- Alt text suggestions
- WCAG compliance

### 8. Base64 Demo (`base64_demo`)
Demonstrates base64 image handling

## Running the Bots

Run the default vision assistant:
```bash
python bots/vision_assistant.py
```

The bot will start on port 8009. Test it with:
```bash
# Text only
curl -X POST "http://localhost:8009/chat" \
  -H "Content-Type: application/json" \
  -d '{"type": "user", "message": "Hello"}'

# With image URL
curl -X POST "http://localhost:8009/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "user",
    "message": "What is in this image?",
    "images": [{"url": "https://example.com/image.jpg"}]
  }'

# With base64 image
curl -X POST "http://localhost:8009/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "user",
    "message": "Describe this",
    "images": [{"base64": "iVBORw0KGgoAAAANS...", "mime_type": "image/png"}]
  }'
```

## Customization

To use a different bot, modify the last line in `vision_assistant.py`:
```python
# Change to any of these:
run_server(screenshot_analyzer, port=8009)
run_server(document_reader, port=8009)
run_server(chart_interpreter, port=8009)
# etc.
```

## Image Input Format

Images can be provided in two ways:

### 1. URL Images
```json
{
  "images": [
    {"url": "https://example.com/image.jpg"}
  ]
}
```

### 2. Base64 Encoded Images
```json
{
  "images": [
    {
      "base64": "iVBORw0KGgoAAAANS...",
      "mime_type": "image/jpeg"
    }
  ]
}
```

## Model Selection

Different models have different strengths:

| Model | Best For | Notes |
|-------|----------|-------|
| GPT-4 Vision | General analysis, code generation | Most versatile |
| Claude 3 | Creative interpretation, detailed analysis | Great for nuanced responses |
| Gemini Vision | Fast responses, technical analysis | Good balance of speed/quality |

## Tips

1. **For Best Results**:
   - Use high-quality images
   - Be specific in your questions
   - Choose the right bot for your task

2. **Multiple Images**:
   - Use the compare bot for side-by-side analysis
   - Order matters - describe image order in your prompt

3. **Performance**:
   - Streaming bots provide faster initial responses
   - Non-streaming bots are better for structured output

## Common Use Cases

- **Development**: Analyze UI screenshots, generate code
- **Documentation**: Extract text from images, create descriptions
- **Accessibility**: Check designs for compliance
- **Analysis**: Interpret charts, compare versions
- **Creative**: Generate stories, artistic interpretations