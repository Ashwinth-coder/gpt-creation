# app.py - AshGPT Terminal Chatbot using Mistral API
from chatbot import chat_with_mistral

print("""
╭──────────────────────────────────────────────╮
│ 🤖 Welcome to BrandTwin AI- Powered by Mistral ✨ │
╰──────────────────────────────────────────────╯
🌟 Type your message below (type 'exit' to quit)
""")

while True:
    user_input = input("You 🌟: ")
    if user_input.lower() == 'exit':
        print("👋 Thanks for chatting with Brand-Twin! Stay legendary 💫")
        break

    response = chat_with_mistral(user_input)
    print(f"AshGPT 🔮: {response}\n")
