import tkinter as tk
from tkinter import scrolledtext
import threading
import os
from groq import Groq
from dotenv import load_dotenv
from app.themes import (APP_BG_CLR, CARD_BG_CLR, APP_TITLE_TXT_CLR, APP_TXT_CLR,
                        BTN_BG_CLR, BTN_TXT_CLR, ENTRY_BG_CLR, ENTRY_TXT_CLR,
                        BODY_FONT, TITLE_FONT, BTN_FONT)
from app.widgets.tabs import create_tabs

load_dotenv()

class ChatScreen:
    def __init__(self, app, parent):
        self.app = app
        self.parent = parent
        self.conversation_history = []
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.create_chat_screen()

    def create_chat_screen(self):
        screen = tk.Frame(self.parent, bg=APP_BG_CLR)
        screen.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.app.add_screen("chat", screen)

        create_tabs(screen, self.app, "chat")

        tk.Label(screen, text="AI Assistant", bg=APP_BG_CLR,
                 fg=APP_TITLE_TXT_CLR, font=TITLE_FONT).pack(pady=(16, 4))
        tk.Label(screen, text="Ask me anything about AI or any topic",
                 bg=APP_BG_CLR, fg=APP_TXT_CLR, font=("Segoe UI", 11)).pack(pady=(0, 12))

        self.chat_display = scrolledtext.ScrolledText(
            screen, wrap="word", width=80, height=18,
            bg=CARD_BG_CLR, fg=APP_TXT_CLR, font=BODY_FONT,
            relief="flat", padx=14, pady=14,
            state="disabled", cursor="arrow",
        )
        self.chat_display.pack(padx=40, pady=(0, 10), fill="both", expand=True)

        self.chat_display.tag_config("user_tag",   foreground="#E0E6F0", font=("Segoe UI", 11, "bold"))
        self.chat_display.tag_config("ai_tag",     foreground="#2B3BFF",  font=("Segoe UI", 11, "bold"))
        self.chat_display.tag_config("msg_tag",    foreground=APP_TXT_CLR, font=BODY_FONT)
        self.chat_display.tag_config("typing_tag", foreground="#4A5568",   font=("Segoe UI", 10, "italic"))
        self.chat_display.tag_config("divider",    foreground="#1E2240")

        input_frame = tk.Frame(screen, bg=APP_BG_CLR)
        input_frame.pack(padx=40, pady=(0, 16), fill="x")

        self.user_input = tk.Text(
            input_frame, height=3,
            bg=ENTRY_BG_CLR, fg=ENTRY_TXT_CLR,
            insertbackground=ENTRY_TXT_CLR,
            font=("Segoe UI", 11), relief="flat",
            padx=12, pady=10, wrap="word",
        )
        self.user_input.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.user_input.bind("<Return>", self.handle_enter)

        tk.Button(
            input_frame, text="Send", font=BTN_FONT,
            bg=BTN_BG_CLR, fg=BTN_TXT_CLR,
            relief="flat", bd=0, padx=20, pady=10,
            cursor="hand2", command=self.send_message,
        ).pack(side="right")

        self.append_message("AI", "Hey! I'm your AI assistant built into Bridge.IT. Ask me anything about AI or any other topic!")

    def handle_enter(self, event):
        if event.state & 0x1:
            return
        self.send_message()
        return "break"

    def append_message(self, sender, message):
        self.chat_display.config(state="normal")
        self.chat_display.insert(tk.END, "\n")
        if sender == "You":
            self.chat_display.insert(tk.END, "You\n", "user_tag")
        else:
            self.chat_display.insert(tk.END, "AI Assistant\n", "ai_tag")
        self.chat_display.insert(tk.END, message + "\n", "msg_tag")
        self.chat_display.insert(tk.END, "─" * 60 + "\n", "divider")
        self.chat_display.config(state="disabled")
        self.chat_display.see(tk.END)

    def show_typing(self):
        self.chat_display.config(state="normal")
        self.chat_display.insert(tk.END, "\nAI Assistant is typing...\n", "typing_tag")
        self.chat_display.config(state="disabled")
        self.chat_display.see(tk.END)

    def remove_typing(self):
        self.chat_display.config(state="normal")
        content = self.chat_display.get("1.0", tk.END)
        typing_text = "\nAI Assistant is typing...\n"
        if typing_text in content:
            start = content.rfind(typing_text)
            start_idx = f"1.0 + {start} chars"
            end_idx = f"1.0 + {start + len(typing_text)} chars"
            self.chat_display.delete(start_idx, end_idx)
        self.chat_display.config(state="disabled")

    def send_message(self):
        user_text = self.user_input.get("1.0", tk.END).strip()
        if not user_text:
            return
        self.user_input.delete("1.0", tk.END)
        self.append_message("You", user_text)
        self.conversation_history.append({"role": "user", "content": user_text})
        self.show_typing()
        thread = threading.Thread(target=self.get_ai_response)
        thread.daemon = True
        thread.start()

    def get_ai_response(self):
        try:
            response = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a helpful AI assistant built into Bridge.IT, "
                            "an app that teaches people about Artificial Intelligence. "
                            "Answer questions about AI concepts, tools, skills, and anything else. "
                            "Keep answers clear, friendly and easy to understand."
                        )
                    }
                ] + self.conversation_history,
                max_tokens=1024,
            )
            ai_reply = response.choices[0].message.content
            self.conversation_history.append({"role": "assistant", "content": ai_reply})
            self.parent.after(0, lambda: self.remove_typing())
            self.parent.after(0, lambda: self.append_message("AI", ai_reply))
        except Exception as e:
            error_msg = str(e)
            self.parent.after(0, lambda: self.remove_typing())
            self.parent.after(0, lambda msg=error_msg: self.append_message("AI", f"Sorry, something went wrong: {msg}"))