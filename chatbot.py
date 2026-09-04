# Basic Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi! How can I help you?"

    elif user_input == "how are you":
        return "I'm fine, thank you!"

    elif user_input == "what is your name":
        return "My name is Python Bot."

    elif user_input == "what can you do":
        return "I can answer some basic questions."

    elif user_input == "thank you":
        return "You're welcome!"

    elif user_input == "bye":
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand that."


print("===== Basic Chatbot =====")
print("Type 'bye' to exit the chatbot.")

while True:
    user_input = input("\nYou: ")

    response = chatbot_response(user_input)

    print("Bot:", response)

    if user_input.lower() == "bye":
        break