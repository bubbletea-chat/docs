"""
Vision/Image Analysis Bot Examples for BubbleTea

These bots demonstrate how to build multimodal AI assistants that can
analyze images using various vision-enabled LLMs.
"""

import os
from bubbletea_chat import chatbot, Text, Markdown, Image, LLM, ImageInput


@chatbot
async def vision_assistant(message: str, images: list = None):
    """
    A general-purpose vision assistant that can analyze any image
    
    Features:
    - Accepts images via URL or base64
    - Provides detailed descriptions
    - Answers questions about images
    - Works with multiple images
    """
    # Use GPT-4 Vision by default (you can change to Claude 3 or Gemini)
    llm = LLM(model="gpt-4-vision-preview", max_tokens=1000)
    
    if not images:
        # No images provided - show instructions
        yield Markdown("""
# 👁️ Vision Assistant

I can analyze and answer questions about images! Here's what I can do:

## 🎯 Capabilities
- **Describe images** in detail
- **Answer questions** about what I see
- **Compare multiple images**
- **Identify objects, people, text**
- **Analyze charts and diagrams**
- **Explain technical drawings**
- **Read and transcribe text**

## 📸 How to use me
1. Upload an image (drag & drop or click to upload)
2. Ask a question about it (optional)
3. I'll analyze and respond!

## 🖼️ Supported formats
- JPEG, PNG, GIF, WebP
- URLs or uploaded files
- Multiple images at once

Try me out with a screenshot, photo, or diagram!
        """)
        return
    
    # Images provided - analyze them
    num_images = len(images)
    
    if num_images == 1:
        yield Text(f"🔍 Analyzing your image...")
    else:
        yield Text(f"🔍 Analyzing {num_images} images...")
    
    # Use streaming for better UX
    async for chunk in llm.stream_with_images(
        message or "Please provide a detailed description of what you see in this image.",
        images
    ):
        yield Text(chunk)


@chatbot(stream=False)
async def screenshot_analyzer(message: str, images: list = None):
    """
    Specialized bot for analyzing screenshots and UI designs
    
    This bot:
    - Identifies UI elements
    - Explains functionality
    - Suggests improvements
    - Can generate code to recreate the UI
    """
    if not images:
        return [
            Markdown("## 🖥️ Screenshot Analyzer"),
            Text("Send me a screenshot of any app, website, or UI and I'll analyze it!"),
            Text(""),
            Text("I can:"),
            Text("• Identify UI components and layouts"),
            Text("• Explain the purpose of different elements"),
            Text("• Suggest UI/UX improvements"),
            Text("• Generate code to recreate the design"),
            Text(""),
            Text("💡 Tip: Ask me to 'generate React code' or 'create HTML/CSS' for the screenshot!")
        ]
    
    llm = LLM(model="gpt-4-vision-preview", temperature=0.3)
    
    # Build appropriate prompt based on user message
    if not message:
        prompt = "Analyze this screenshot. Identify the UI components, layout structure, and purpose of the interface."
    elif "code" in message.lower():
        if "react" in message.lower():
            prompt = "Generate React component code that recreates this UI design. Include proper styling."
        elif "html" in message.lower() or "css" in message.lower():
            prompt = "Generate HTML and CSS code that recreates this UI design exactly."
        else:
            prompt = f"Generate code to recreate this UI. {message}"
    else:
        prompt = message
    
    # Get complete analysis
    response = await llm.acomplete_with_images(prompt, images)
    
    return [
        Markdown("## 🖥️ Screenshot Analysis"),
        Markdown(response),
        Text(""),
        Text("Need something else? Try asking for:"),
        Text("• 'Generate React code for this'"),
        Text("• 'What could be improved in this UI?'"),
        Text("• 'Explain the user flow'")
    ]


@chatbot
async def document_reader(message: str, images: list = None):
    """
    OCR and document analysis bot
    
    Extracts and analyzes text from:
    - Photos of documents
    - Handwritten notes
    - Forms and receipts
    - Books and articles
    """
    if not images:
        yield Markdown("""
## 📄 Document Reader Bot

I can read and analyze text from images! Send me:

- 📝 **Handwritten notes** - I'll transcribe them
- 📋 **Forms & documents** - Extract all text and data
- 🧾 **Receipts & invoices** - Parse amounts and details  
- 📚 **Book pages** - Read and summarize content
- 🏷️ **Labels & signs** - Extract text from photos

### Special abilities:
- Multi-language support
- Table extraction
- Form field identification
- Handwriting recognition

Just upload an image containing text!
        """)
        return
    
    llm = LLM(model="gpt-4-vision-preview", temperature=0.1)  # Low temp for accuracy
    
    prompt = message if message else "Please extract and transcribe all text from this image. If it's a form or structured document, preserve the structure."
    
    yield Text("📖 Reading document...")
    
    async for chunk in llm.stream_with_images(prompt, images):
        yield Text(chunk)


@chatbot
async def chart_interpreter(message: str, images: list = None):
    """
    Data visualization and chart analysis bot
    
    Interprets:
    - Bar charts, line graphs, pie charts
    - Technical diagrams
    - Flowcharts and mind maps
    - Scientific plots
    """
    if not images:
        yield Markdown("""
## 📊 Chart & Diagram Interpreter

I specialize in analyzing data visualizations and diagrams!

### What I can analyze:
- 📊 **Charts & Graphs**: Bar, line, pie, scatter plots
- 🔀 **Flowcharts**: Process flows and decision trees
- 🗺️ **Mind Maps**: Concept relationships
- 📈 **Technical Diagrams**: Architecture, networks, systems
- 🔬 **Scientific Plots**: Research data, measurements

### I can help you:
- Understand trends and patterns
- Extract specific data points
- Explain relationships
- Summarize key insights
- Identify anomalies

Upload a chart or diagram to get started!
        """)
        return
    
    llm = LLM(model="claude-3-sonnet-20240229", temperature=0.3)
    
    if not message:
        prompt = "Analyze this chart/diagram. Explain what it shows, identify key trends or patterns, and provide insights about the data."
    else:
        prompt = message
    
    yield Text("📊 Analyzing visualization...")
    
    response = await llm.acomplete_with_images(prompt, images)
    yield Markdown(response)


@chatbot(stream=False)
async def multi_image_compare(message: str, images: list = None):
    """
    Compares multiple images to find similarities and differences
    
    Great for:
    - Before/after comparisons
    - Product comparisons
    - Design variations
    - Progress tracking
    """
    if not images:
        return [
            Markdown("## 🔄 Multi-Image Comparison Bot"),
            Text("Send me 2 or more images and I'll compare them!"),
            Text(""),
            Text("Perfect for:"),
            Text("• Before/after photos"),
            Text("• Product comparisons"),
            Text("• Design A/B testing"),
            Text("• Progress documentation"),
            Text("• Spot the differences"),
            Text(""),
            Text("Upload multiple images to start comparing!")
        ]
    
    if len(images) < 2:
        return Text("Please upload at least 2 images for comparison!")
    
    llm = LLM(model="gpt-4-vision-preview", temperature=0.5)
    
    prompt = message if message else f"Compare these {len(images)} images. Identify similarities, differences, and any notable changes or patterns between them."
    
    response = await llm.acomplete_with_images(prompt, images)
    
    return [
        Markdown(f"## 🔄 Comparison of {len(images)} Images"),
        Markdown(response),
        Text(""),
        Text(f"Analyzed {len(images)} images successfully!")
    ]


@chatbot
async def creative_interpreter(message: str, images: list = None):
    """
    Creative and artistic interpretation of images
    
    Provides:
    - Artistic analysis
    - Creative descriptions
    - Story generation from images
    - Mood and emotion detection
    """
    if not images:
        yield Markdown("""
## 🎨 Creative Image Interpreter

I provide artistic and creative interpretations of images!

### What I offer:
- 🎭 **Artistic Analysis**: Style, composition, techniques
- ✍️ **Creative Writing**: Stories inspired by images
- 🎨 **Design Critique**: Color, balance, visual impact
- 😊 **Emotion Detection**: Mood and feeling analysis
- 🌈 **Style Description**: Artistic movements and influences

### Try asking me to:
- "Write a story about this image"
- "Analyze the artistic style"
- "Describe the mood and emotions"
- "Create a poem inspired by this"

Upload an image to unlock its creative potential!
        """)
        return
    
    llm = LLM(model="claude-3-sonnet-20240229", temperature=0.9)  # High temp for creativity
    
    if not message:
        prompt = "Provide a creative and artistic interpretation of this image. Describe its mood, emotions, and any stories it might tell."
    elif "story" in message.lower():
        prompt = "Write a creative short story inspired by this image."
    elif "poem" in message.lower():
        prompt = "Create a poem inspired by this image."
    else:
        prompt = message
    
    yield Text("🎨 Creating artistic interpretation...")
    
    async for chunk in llm.stream_with_images(prompt, images):
        yield Text(chunk)


@chatbot
async def accessibility_checker(message: str, images: list = None):
    """
    Checks images and UIs for accessibility issues
    
    Evaluates:
    - Color contrast
    - Text readability
    - Alt text suggestions
    - UI accessibility
    """
    if not images:
        yield Markdown("""
## ♿ Accessibility Checker

I help ensure your images and UIs are accessible to everyone!

### What I check:
- 🎨 **Color Contrast**: WCAG compliance
- 📝 **Text Readability**: Font sizes and clarity
- 🖼️ **Alt Text**: Suggestions for image descriptions
- 🔘 **UI Elements**: Button sizes, touch targets
- 👁️ **Visual Clarity**: For users with visual impairments

### I can help with:
- Website screenshots
- App interfaces
- Marketing materials
- Infographics
- Any visual content

Upload an image to check its accessibility!
        """)
        return
    
    llm = LLM(model="gpt-4-vision-preview", temperature=0.3)
    
    prompt = """Analyze this image for accessibility concerns. Check for:
1. Color contrast issues
2. Text readability
3. UI element sizes and spacing
4. Any potential barriers for users with disabilities
5. Suggest improvements and provide alt text recommendation."""
    
    if message:
        prompt = f"{prompt}\n\nAdditional context: {message}"
    
    yield Text("♿ Checking accessibility...")
    
    response = await llm.acomplete_with_images(prompt, images)
    yield Markdown(response)


# Example showing base64 image handling
@chatbot
async def base64_demo(message: str, images: list = None):
    """
    Demonstrates handling of base64 encoded images
    """
    if not images:
        yield Text("This bot demonstrates base64 image handling.")
        yield Text("Upload an image to see how it's processed!")
        return
    
    # Log image format for demo purposes
    for i, img in enumerate(images):
        if img.base64:
            yield Text(f"✅ Image {i+1}: Received as base64 encoded data")
            if img.mime_type:
                yield Text(f"   MIME type: {img.mime_type}")
        elif img.url:
            yield Text(f"✅ Image {i+1}: Received as URL")
            yield Text(f"   URL: {img.url[:50]}...")
    
    yield Text("")
    yield Text("🤖 Now analyzing with AI...")
    
    llm = LLM(model="gpt-4-vision-preview")
    response = await llm.acomplete_with_images(
        message or "What's in this image?",
        images
    )
    
    yield Markdown(response)


if __name__ == "__main__":
    # Run the general vision assistant by default
    from bubbletea_chat import run_server
    run_server(vision_assistant, port=8009)