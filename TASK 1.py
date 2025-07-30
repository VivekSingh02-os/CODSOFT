import re

def chatbot():
    print("🤖 Chatbot: Hello! I'm ChatBot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("🤖 Chatbot: Goodbye! Have a nice day. 😊")
            break

        elif re.search(r"\b(hi|hello|hey)\b", user_input):
            print("🤖 Chatbot: Hello there! How can I help you today?")

        elif re.search(r"\b(how are you|how are you doing)\b", user_input):
            print("🤖 Chatbot: I'm just a program, but I'm functioning well. Thanks for asking!")

        elif re.search(r"\b(who are you|what is your name)\b", user_input):
            print("🤖 Chatbot: I'm a simple chatbot created to chat with you.")

        elif re.search(r"\b(help|support|assist)\b", user_input):
            print("🤖 Chatbot: Sure! I'm here to help. Ask me anything.")

        elif re.search(r"\b(thank you|thanks)\b", user_input):
            print("🤖 Chatbot: You're welcome! 😊")

        else:
            print("🤖 Chatbot: Sorry, I didn't understand that. Can you please rephrase? or provide more details.")

chatbot()