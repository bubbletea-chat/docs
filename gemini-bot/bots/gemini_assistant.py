"""
Non-streaming Google Gemini Assistant Bot

This bot demonstrates how to use Google's Gemini models without streaming.
Perfect for when you need complete responses before displaying them.
"""

import os
from bubbletea_chat import chatbot, Text, Markdown, Image, LLM


@chatbot(stream=False)
async def gemini_assistant(prompt: str):
    """
    A helpful AI assistant powered by Google's Gemini Pro
    
    This bot:
    - Uses Gemini Pro for balanced performance
    - Returns complete responses at once
    - Good for general-purpose assistance
    
    Make sure to set your Google API key:
    export GEMINI_API_KEY=your-api-key-here
    """
    # Initialize with Gemini Pro
    llm = LLM(model="gemini/gemini-pro", temperature=0.7)
    
    # Get the complete response
    response = await llm.acomplete(prompt)
    
    return Text(response)


@chatbot(stream=False)
async def gemini_flash_assistant(prompt: str):
    """
    A fast assistant using Gemini Flash
    
    This bot:
    - Uses Gemini 1.5 Flash for rapid responses
    - Optimized for speed while maintaining quality
    - Returns formatted responses
    """
    llm = LLM(model="gemini/gemini-1.5-flash", temperature=0.5)
    
    # Get the response
    response = await llm.acomplete(prompt)
    
    # Return with metadata
    return [
        Markdown(f"""
## Gemini Flash Response

{response}

---
*Model: Gemini 1.5 Flash | Response time optimized*
        """)
    ]


@chatbot(stream=False)
async def gemini_analyst(prompt: str):
    """
    An analytical assistant using Gemini Pro
    
    This bot:
    - Provides structured, analytical responses
    - Uses lower temperature for consistency
    - Formats responses with clear sections
    """
    llm = LLM(
        model="gemini/gemini-pro",
        temperature=0.3,  # Lower for analytical tasks
        max_tokens=2000
    )
    
    # Add analytical context
    messages = [
        {
            "role": "system",
            "content": "You are an analytical assistant. Break down topics systematically, provide data-driven insights, and structure your responses with clear sections and bullet points."
        },
        {"role": "user", "content": prompt}
    ]
    
    # Get structured response
    response = llm.with_messages(messages)
    
    return Markdown(response)


@chatbot(stream=False)
async def gemini_creative_bot(prompt: str):
    """
    A creative assistant using Gemini with higher temperature
    
    This bot:
    - Generates creative content
    - Uses higher temperature for variety
    - Returns multiple creative variations
    """
    llm = LLM(
        model="gemini/gemini-pro",
        temperature=0.9,  # Higher for creativity
        max_tokens=1500
    )
    
    # Generate main creative response
    response = await llm.acomplete(f"Create something creative based on: {prompt}")
    
    # Generate a variation
    variation_prompt = f"Create a different creative take on: {prompt}"
    variation = await llm.acomplete(variation_prompt)
    
    return [
        Markdown("## Creative Response #1"),
        Text(response),
        Text(""),
        Markdown("## Creative Variation #2"),
        Text(variation),
        Markdown("---"),
        Text("🎨 Generated with Gemini's creative mode")
    ]


@chatbot(stream=False)
async def gemini_educator(prompt: str):
    """
    An educational assistant that explains concepts clearly
    
    This bot:
    - Breaks down complex topics
    - Provides examples and analogies
    - Structures learning content
    """
    llm = LLM(
        model="gemini/gemini-pro",
        temperature=0.5,
        max_tokens=2500
    )
    
    # Educational system prompt
    messages = [
        {
            "role": "system",
            "content": "You are an expert educator. Explain concepts clearly with examples, analogies, and step-by-step breakdowns. Use formatting to enhance learning."
        },
        {"role": "user", "content": prompt}
    ]
    
    # Get educational content
    response = llm.with_messages(messages)
    
    # Add a visual element if relevant
    components = [
        Markdown("## 📚 Educational Explanation"),
        Markdown(response)
    ]
    
    # Add an illustrative image for certain topics
    if any(word in prompt.lower() for word in ["diagram", "chart", "visual", "graph"]):
        components.extend([
            Text(""),
            Text("Here's a visual representation:"),
            Image(
                "https://source.unsplash.com/800x400/?education,diagram",
                alt="Educational diagram"
            )
        ])
    
    return components


if __name__ == "__main__":
    # Run the Gemini assistant by default
    from bubbletea_chat import run_server
    run_server(gemini_assistant, port=8006)