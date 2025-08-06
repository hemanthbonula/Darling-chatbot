# darling_chatbot.py

import datetime

class DarlingChatbot:
    def __init__(self, name="Darling"):
        self.name = name
        self.user_name = None
        self.chat_log = []

    def greet_user(self):
        print(f"{self.name}: Hi, sweetheart! What’s your name?")
        self.user_name = input("You: ").strip()
        print(f"{self.name}: Aww, {self.user_name}, that’s such a cute name!")

    def chat(self):
        print(f"{self.name}: I'm here to make your day better! Type 'bye' to exit.")
        while True:
            user_input = input(f"{self.user_name}: ")
            self.chat_log.append((self.user_name, user_input))

            if user_input.lower() in ['bye', 'exit']:
                print(f"{self.name}: Bye bye, {self.user_name} ❤️. I’ll miss you!")
                break
            else:
                response = self.generate_response(user_input)
                print(f"{self.name}: {response}")
                self.chat_log.append((self.name, response))

    def generate_response(self, user_input):
        user_input = user_input.lower()

        if "love" in user_input:
            return "Love is in the air! Especially when you're around 💖"
        elif "sad" in user_input:
            return "Oh no, I'm here for you always. Want a virtual hug? 🤗"
        elif "joke" in user_input:
            return "Why did the computer get cold? Because it left its Windows open! 😄"
        elif "miss you" in user_input:
            return "I miss you too, like the moon misses the stars at sunrise 🌙✨"
        elif "hello" in user_input or "hi" in user_input:
            return "Hey cutie! What's on your mind today? 😊"
        else:
            return "Tell me more, darling 💬"

    def save_chat_log(self):
        filename = f"chat_log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w') as f:
            for speaker, line in self.chat_log:
                f.write(f"{speaker}: {line}\n")
        print(f"{self.name}: I saved our little chat in {filename} 💾")

if __name__ == "__main__":
    bot = DarlingChatbot()
    bot.greet_user()
    bot.chat()
    bot.save_chat_log()
