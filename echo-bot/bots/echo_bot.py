"""
Echo Bot - Simple non-streaming bot for testing basic functionality
"""

import sys
import os
import random

# Add BubbleTea package to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'bubbletea'))

try:
    import bubbletea as bt
except ImportError as e:
    print(f"❌ Failed to import BubbleTea: {e}")
    print("Make sure the bubbletea package is available")
    sys.exit(1)

# Sample images for testing
SAMPLE_IMAGES = [
    "https://picsum.photos/400/300?random=1",
    "https://picsum.photos/400/300?random=2", 
    "https://picsum.photos/400/300?random=3",
    "https://source.unsplash.com/400x300/?nature",
    "https://source.unsplash.com/400x300/?technology",
]

@bt.chatbot(name="echo-bot", stream=False)
def echo_bot(message: str):
    """
    Simple echo bot that returns all responses at once
    
    Features:
    - Message echo and analysis
    - Conditional image display
    - Non-streaming response
    """
    
    responses = []
    
    # Basic echo
    responses.append(bt.Text(f"🔄 Echo: {message}"))
    
    # Message analysis
    word_count = len(message.split())
    char_count = len(message)
    has_question = "?" in message
    has_exclamation = "!" in message
    
    responses.append(bt.Markdown(f"""
## 📊 Message Analysis
- **Words**: {word_count}
- **Characters**: {char_count}
- **Contains question**: {"Yes" if has_question else "No"}
- **Contains exclamation**: {"Yes" if has_exclamation else "No"}
- **Uppercase ratio**: {sum(1 for c in message if c.isupper()) / len(message) * 100:.1f}%
    """))
    
    # Conditional responses based on message content
    if any(word in message.lower() for word in ["image", "picture", "photo", "show"]):
        responses.append(bt.Text("🖼️ I see you want an image! Here you go:"))
        responses.append(bt.Image(
            random.choice(SAMPLE_IMAGES),
            alt="Random image based on your request"
        ))
    
    if any(word in message.lower() for word in ["help", "what", "how"]):
        responses.append(bt.Markdown("""
### 🆘 Echo Bot Help
I'm a simple echo bot that can:
- Echo back your messages
- Analyze message statistics  
- Show images when requested
- Respond instantly (non-streaming)
        """))
    
    responses.append(bt.Text("What would you like to do next?"))
    
    # Add timestamp info
    from datetime import datetime
    responses.append(bt.Markdown(f"""
---
*Response generated at {datetime.now().strftime("%H:%M:%S")} • Non-streaming mode*
    """))
    
    return responses


if __name__ == "__main__":
    print("🔄 Starting Echo Bot...")
    print("Server: http://localhost:8000")
    print("Test: curl -X POST 'http://localhost:8000/chat' -H 'Content-Type: application/json' -d '{\"type\": \"user\", \"message\": \"Hello echo bot!\"}'")
    
    bt.run_server(echo_bot, port=8000)