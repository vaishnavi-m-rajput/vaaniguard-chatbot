import tkinter as tk
from chat import get_response  # Make sure this is defined in chat.py

class ChatBotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("VaaniGuard 💬")
        self.root.geometry("500x550")
        self.root.configure(bg="#f5f5f5")

        self.chat_log = tk.Text(root, bd=0, bg="white", height=8, width=50, font=("Arial", 12))
        self.chat_log.config(state=tk.DISABLED)
        self.chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.entry_box = tk.Entry(root, bd=0, bg="white", font=("Arial", 14))
        self.entry_box.pack(fill=tk.X, padx=10, pady=(0, 10))
        self.entry_box.bind("<Return>", self.send_message)

        self.send_button = tk.Button(root, text="Send", width=12, command=self.send_message, bg="#4CAF50", fg="white")
        self.send_button.pack(pady=(0, 10))

        self.insert_bot_message("VaaniGuard 🤖 is online! Say something, love...")

    def insert_bot_message(self, message):
        self.chat_log.config(state=tk.NORMAL)
        self.chat_log.insert(tk.END, "VaaniGuard: " + message + "\n\n")
        self.chat_log.config(state=tk.DISABLED)
        self.chat_log.yview(tk.END)

    def insert_user_message(self, message):
        self.chat_log.config(state=tk.NORMAL)
        self.chat_log.insert(tk.END, "You: " + message + "\n")
        self.chat_log.config(state=tk.DISABLED)
        self.chat_log.yview(tk.END)

    def send_message(self, event=None):
        user_input = self.entry_box.get()
        if user_input.strip() == "":
            return
        self.insert_user_message(user_input)
        response = get_response(user_input)
        self.insert_bot_message(response)
        self.entry_box.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatBotApp(root)
    root.mainloop()
