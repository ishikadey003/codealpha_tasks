"""
CodeAlpha Internship - Task 4: Basic Chatbot
"""


def get_response(user_input):
    """Return a reply based on keywords found in the user's message."""
    text = user_input.lower().strip()

    if "hello" in text or "hi" in text:
        return "Hi! How can I help you today?"
    elif "how are you" in text:
        return "I'm fine, thanks! How about you?"
    elif "name" in text:
        return "I'm a simple chatbot built for the CodeAlpha internship."
    elif "help" in text:
        return "You can talk to me by typing things like 'hello', 'how are you', or 'bye'."
    elif "bye" in text:
        return "Goodbye! Have a great day."
    else:
        return "Sorry, I didn't understand that. Try saying 'hello' or 'help'."


def run_chatbot():
    print("Chatbot: Hi! Type 'bye' anytime to exit.\n")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Chatbot:", response)

        if "bye" in user_input.lower():
            break


if __name__ == "__main__":
    run_chatbot()
