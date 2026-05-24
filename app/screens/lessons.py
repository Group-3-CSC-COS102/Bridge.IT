import tkinter as tk
from tkinter import messagebox
from app.themes import (APP_BG_CLR, CARD_BG_CLR, APP_TITLE_TXT_CLR, APP_TXT_CLR,
                        BTN_BG_CLR, BTN_TXT_CLR, BORDER_CLR, TITLE_FONT, BODY_FONT, BTN_FONT)
from app.widgets.tabs import create_tabs
from app.storage.lesson import load_lessons

class LessonsScreens:
    def __init__(self, app, parent):
        self.app = app
        self.parent = parent
        self.create_lessons_screen()

    def create_lessons_screen(self):
        screen = tk.Frame(self.parent, bg=APP_BG_CLR)
        screen.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.app.add_screen("lessons", screen)

        create_tabs(screen, self.app, "lessons")

        tk.Label(screen, text="Basics of AI", bg=APP_BG_CLR,
                 fg=APP_TITLE_TXT_CLR, font=TITLE_FONT).pack(pady=(20, 4))

        self.section_title = tk.Label(screen, text="", bg=APP_BG_CLR,
                                      fg=APP_TXT_CLR, font=("Segoe UI", 13))
        self.section_title.pack(pady=(0, 12))

        self.section_text = tk.Text(
            screen, width=80, height=12, wrap="word",
            bg=CARD_BG_CLR, fg=APP_TXT_CLR,
            font=BODY_FONT, relief="flat",
            padx=20, pady=16,
            selectbackground=BTN_BG_CLR,
        )
        self.section_text.pack(padx=40, pady=(0, 16))
        self.section_text.config(state="disabled")

        controls = tk.Frame(screen, bg=APP_BG_CLR)
        controls.pack()

        for text, cmd in [("  ← Previous  ", self.prev_lesson), ("  Next →  ", self.next_lesson)]:
            tk.Button(controls, text=text, font=BTN_FONT,
                      bg=BTN_BG_CLR, fg=BTN_TXT_CLR,
                      relief="flat", bd=0, padx=16, pady=8,
                      cursor="hand2", command=cmd).pack(side="left", padx=6)

        self.lessons = []
        self.lesson_index = 0
        self.get_lessons()
        self.current_section()

    def get_lessons(self):
        df = load_lessons()
        if df is None or df.empty:
            self.lessons = []
            return
        self.lessons = []
        for _, row in df.iterrows():
            title   = row.get("title", "").strip()
            content = row.get("content", "").strip()
            if not title and not content:
                continue
            self.lessons.append({"title": title, "content": content})

    def current_section(self):
        if not self.lessons:
            self.section_title.config(text="No lessons available")
            self.section_text.config(state="normal")
            self.section_text.delete("1.0", tk.END)
            self.section_text.config(state="disabled")
            return
        section = self.lessons[self.lesson_index]
        n = self.lesson_index + 1
        self.section_title.config(text=f"Section {n} of {len(self.lessons)}: {section['title']}")
        self.section_text.config(state="normal")
        self.section_text.delete("1.0", tk.END)
        self.section_text.insert(tk.END, section["content"])
        self.section_text.config(state="disabled")

    def next_lesson(self):
        if self.lesson_index == len(self.lessons) - 1:
            messagebox.showinfo("Info", "This is the last section.")
            return
        self.lesson_index += 1
        self.current_section()

    def prev_lesson(self):
        if self.lesson_index == 0:
            messagebox.showinfo("Info", "This is the first section.")
            return
        self.lesson_index -= 1
        self.current_section()