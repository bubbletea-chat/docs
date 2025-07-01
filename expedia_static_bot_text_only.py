# expedia_static_bot_text_only.py

from bubbletea_chat import bt, run_server

conversation = [
    {
        "sender": "agent",
        "content": bt.Text("Hi Ash! Ready to plan a trip?\n\n(Please reply: Flights)")
    },
    {
        "sender": "user",
        "expected": "Flights"
    },
    {
        "sender": "agent",
        "content": bt.Text("Great. Where are you flying from and to?\n\n(Please reply: From JFK to LAX)")
    },
    {
        "sender": "user",
        "expected": "From JFK to LAX"
    },
    {
        "sender": "agent",
        "content": bt.Text("And your travel dates?\n\n(Please reply: Jul 12 – Jul 16)")
    },
    {
        "sender": "user",
        "expected": "Jul 12 – Jul 16"
    },
    {
        "sender": "agent",
        "content": bt.Text(
            "Here are some options for round-trip flights JFK → LAX:\n\n"
            "1. Delta – Nonstop, 9:30am–12:30pm, $278\n"
            "2. JetBlue – 11:00am–2:05pm, Free Wi-Fi, $265\n"
            "3. United – 1 stop, 8:00am–1:45pm, $240\n\n"
            "(Please reply: JetBlue)"
        )
    },
    {
        "sender": "user",
        "expected": "JetBlue"
    },
    {
        "sender": "agent",
        "content": bt.Text("Great! Do you want to add a hotel too?\n\n(Please reply: No, just flight)")
    },
    {
        "sender": "user",
        "expected": "No, just flight"
    },
    {
        "sender": "agent",
        "content": bt.Text(
            "Final details:\n"
            "- JetBlue, JFK → LAX\n"
            "- Jul 12–Jul 16\n"
            "- $265 round-trip\n\n"
            "Ready to book?\n\n(Please reply: Confirm)"
        )
    },
    {
        "sender": "user",
        "expected": "Confirm"
    },
    {
        "sender": "agent",
        "content": bt.Text("✅ Booking confirmed! Have a great trip, Ash.")
    },
]

@bt.chatbot
def expedia_bot():
    for step in conversation:
        if step["sender"] == "agent":
            yield step["content"]
        elif step["sender"] == "user":
            user_input = yield
            while user_input.strip() != step["expected"]:
                yield bt.Text(f"Please type exactly: {step['expected']}")
                user_input = yield

if __name__ == "__main__":
    run_server(expedia_bot)
