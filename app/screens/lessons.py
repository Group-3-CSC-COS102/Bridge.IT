import tkinter as tk
from tkinter import messagebox

from app.themes import APP_BG_CLR, APP_TITLE_TXT_CLR, APP_TXT_CLR, BTN_BG_CLR, BTN_TXT_CLR, TITLE_FONT
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

        #page header
        tk.Label(screen, text=f"Basics of AI", bg=APP_BG_CLR, fg=APP_TITLE_TXT_CLR, font=TITLE_FONT).pack(pady=(10,6))

        #Title of lesson section
        self.section_title = tk.Label(screen, text="", bg=APP_BG_CLR, fg=APP_TXT_CLR, font=TITLE_FONT)
        self.section_title.pack(pady=(0, 6))

        #Text area for lesson content
        self.section_text = tk.Text(screen, width=80, height=12, wrap="word", bg="white", fg="black")
        self.section_text.pack(pady=(0, 10))
        self.section_text.config(state="disabled") #Can't be edited in-app

        #Control Frame
        controls = tk.Frame(screen, bg=APP_BG_CLR)
        controls.pack(pady=10)

        #Buttons in control frame
        tk.Button(controls, text="<", bg=BTN_BG_CLR, fg=BTN_TXT_CLR, command=self.prev_lesson).grid(row=0, column=0, padx=6)
        tk.Button(controls, text=">", bg=BTN_BG_CLR, fg=BTN_TXT_CLR, command=self.next_lesson).grid(row=0, column=1, padx=6)

        self.lessons = []
        self.lesson_index = 0
        self.get_lessons()
        self.current_section()

    #Gets lessons from CSV and stores in self.lessons
    def get_lessons(self):
        df = load_lessons()

        #Checks if df is None or empty
        if df is None or df.empty:
            self.lessons = []
            return

        self.lessons = []
        for index, row in df.iterrows():
            section_id = row.get("section_id", "").strip()
            title = row.get("title", "").strip()
            content = row.get("content", "").strip()
            if not title and not content:
                continue
            self.lessons.append({"section_id": section_id, "title": title, "content": content})

    #Loads current lesson section into the UI
    def current_section(self):
        #Failsafe if self.lessons is empty
        if not self.lessons:
            self.section_title.config(text="No lessons available")
            self.section_text.config(state="normal")
            self.section_text.delete("1.0", tk.END)
            self.section_text.config(state="disabled")
            return

        section = self.lessons[self.lesson_index]
        n = self.lesson_index + 1
        self.section_title.config(text=f"Section {n}: {section['title']}")
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