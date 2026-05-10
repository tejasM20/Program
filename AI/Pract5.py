def chatbot():
    print("Chatbot: Hello! How can I help you? (Type 'bye' to exit)")

    while True:
        user_input = input("User: ").lower()

        if "hi" in user_input or "hello" in user_input:
            print("Chatbot: Hello! How may I assist you?")

        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm doing great! 😊")

        elif "name" in user_input:
            print("Chatbot: I am a simple Python chatbot.")

        elif "price" in user_input or "cost" in user_input:
            print("Chatbot: Please visit our website for pricing details.")

        elif "contact" in user_input or "support" in user_input:
            print("Chatbot: You can contact us at support@example.com")

        elif "services" in user_input:
            print("Chatbot: We provide AI, Web Development, and Data Science services.")

        elif "time" in user_input:
            from datetime import datetime
            now = datetime.now()
            print("Chatbot: Current time is", now.strftime("%H:%M:%S"))

        elif "date" in user_input:
            from datetime import datetime
            today = datetime.now()
            print("Chatbot: Today's date is", today.strftime("%Y-%m-%d"))

        elif "bye" in user_input or "exit" in user_input:
            print("Chatbot: Thank you! Have a nice day.")
            break

        else:
            print("Chatbot: Sorry, I did not understand your query.")


# Run chatbot
chatbot()