from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

# Create chatbot instance
chatbot = ChatBot("Darling")

# Train chatbot with English corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# GUI Application
class DarlingChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Darling Chatbot")
        self.root.geometry("500x550")
        self.root.resizable(False, False)

        # Header
        header = tk.Label(root, text="Darling Chatbot 💬", font=("Helvetica", 16, "bold"), pady=10)
        header.pack()

        # Chat window
        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, font=("Arial", 12))
        self.chat_area.pack(padx=10, pady=5)
        self.chat_area.config(state=tk.DISABLED)

        # User input
        self.entry = tk.Entry(root, width=40, font=("Arial", 12))
        self.entry.pack(pady=10, padx=10, side=tk.LEFT, expand=True, fill=tk.X)
        self.entry.bind("<Return>", self.send_message)

        # Send button
        send_button = tk.Button(root, text="Send", command=self.send_message, font=("Arial", 12), bg="lightblue")
        send_button.pack(pady=10, padx=10, side=tk.RIGHT)

    def send_message(self, event=None):
        user_input = self.entry.get().strip()
        if not user_input:
            messagebox.showwarning("Empty Input", "Please type a message.")
            return

        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.insert(tk.END, "You: " + user_input + "\n")

        try:
            response = chatbot.get_response(user_input)
            self.chat_area.insert(tk.END, "Darling: " + str(response) + "\n\n")
        except Exception as e:
            self.chat_area.insert(tk.END, "Darling: Sorry, I couldn't process that.\n\n")

        self.chat_area.config(state=tk.DISABLED)
        self.entry.delete(0, tk.END)
        self.chat_area.see(tk.END)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = DarlingChatbotApp(root)
    root.mainloop()

