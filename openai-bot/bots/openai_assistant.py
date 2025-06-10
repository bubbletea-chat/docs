"""
Non-streaming OpenAI GPT Assistant Bot

This bot demonstrates how to use OpenAI's GPT models without streaming.
The entire response is generated before being sent to the user.
"""

import os
from bubbletea_chat import chatbot, Text, Markdown, LLM


@chatbot(stream=False)  # Explicitly disable streaming
async def gpt_assistant(prompt: str):
    """
    A helpful AI assistant powered by OpenAI's GPT-4
    
    This bot:
    - Uses GPT-4 for high-quality responses
    - Returns the complete response at once (no streaming)
    - Good for when you need the full response before displaying
    
    Make sure to set your OpenAI API key:
    export OPENAI_API_KEY=your-api-key-here
    """
    # Initialize the LLM with GPT-4
    llm = LLM(model="gpt-4", temperature=0.7)
    
    # Get the complete response
    response = await llm.acomplete(prompt)
    
    # Return the response as a single text component
    return Text(response)


@chatbot(stream=False)
async def gpt_turbo_assistant(prompt: str):
    """
    A faster assistant using GPT-3.5-turbo
    
    This bot:
    - Uses GPT-3.5-turbo for faster, cost-effective responses
    - Returns formatted markdown responses
    - Includes response metadata
    """
    llm = LLM(model="gpt-3.5-turbo", temperature=0.5)
    
    # Get the response
    response = await llm.acomplete(prompt)
    
    # Return formatted response with metadata
    return [
        Markdown(f"""
## GPT-3.5 Turbo Response

{response}

---
*Model: GPT-3.5-turbo | Non-streaming mode*
        """)
    ]


@chatbot(stream=False)
async def code_assistant(prompt: str):
    """
    A specialized code assistant using GPT-4
    
    This bot:
    - Optimized for programming questions
    - Returns code with proper formatting
    - Uses lower temperature for accuracy
    """
    llm = LLM(
        model="gpt-4",
        temperature=0.3,  # Lower temperature for more precise code
        max_tokens=2000
    )
    
    # Add a system message for code assistance
    messages = [
        {
            "role": "system", 
            "content": "You are an expert programming assistant. Provide clear, concise code examples with explanations. Always use markdown code blocks with appropriate language tags."
        },
        {"role": "user", "content": prompt}
    ]
    
    # Get the complete response
    response = llm.with_messages(messages)
    
    # Return as markdown for better code formatting
    return Markdown(response)


@chatbot(stream=False)
async def multi_response_bot(prompt: str):
    """
    A bot that returns multiple components at once
    
    This bot demonstrates:
    - Using multiple LLM calls
    - Returning multiple components
    - Different response formats
    """
    llm = LLM(model="gpt-3.5-turbo", temperature=0.7)
    
    # Get main response
    main_response = await llm.acomplete(prompt)
    
    # Generate a summary
    summary_prompt = f"Provide a one-sentence summary of this response: {main_response}"
    summary = await llm.acomplete(summary_prompt)
    
    # Return multiple components
    return [
        Text("📝 Summary:"),
        Text(summary),
        Text(""),  # Empty line
        Markdown("### Full Response:"),
        Text(main_response),
        Markdown("---"),
        Text("💡 This response was generated in non-streaming mode with multiple components.")
    ]


if __name__ == "__main__":
    # Run the GPT assistant by default
    from bubbletea_chat import run_server
    run_server(gpt_assistant, port=8005)