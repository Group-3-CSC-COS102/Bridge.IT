import tkinter as tk
from tkinter import messagebox

from app.themes import APP_BG_CLR, APP_TITLE_TXT_CLR, APP_TXT_CLR, BTN_BG_CLR, BTN_TXT_CLR, TITLE_FONT
from app.widgets.tabs import create_tabs
from app.storage.skill import load_skills


class SkillsScreens:
    def __init__(self, app, parent):
        self.app = app
        self.parent = parent

        self.create_skills_screen()

    def create_skills_screen(self):
        screen = tk.Frame(self.parent, bg=APP_BG_CLR)
        screen.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.app.add_screen("skills", screen)

        create_tabs(screen, self.app, "skills")

        #page header
        tk.Label(screen, text="AI Skills", bg=APP_BG_CLR, fg=APP_TITLE_TXT_CLR, font=TITLE_FONT).pack(pady=(10, 6))

        #Title of section
        self.section_title = tk.Label(screen, text="", bg=APP_BG_CLR, fg=APP_TXT_CLR, font=TITLE_FONT)
        self.section_title.pack(pady=(0, 6))

        #Text area for section content
        self.section_text = tk.Text(screen, width=80, height=20, wrap="word", bg="white", fg="black")
        self.section_text.pack(pady=(0, 10))
        self.section_text.config(state="disabled") #Can't be edited in-app

        #Control Frame
        controls = tk.Frame(screen, bg=APP_BG_CLR)
        controls.pack(pady=10)

        #Buttons in control frame
        tk.Button(controls, text="<", bg=BTN_BG_CLR, fg=BTN_TXT_CLR, command=self.prev_section).grid(row=0, column=0, padx=6)
        tk.Button(controls, text=">", bg=BTN_BG_CLR, fg=BTN_TXT_CLR, command=self.next_section).grid(row=0, column=1, padx=6)

        self.skills = []
        self.skill_index = 0
        self.get_skills()
        self.current_section()

    def get_skills(self):
        df = load_skills()

        #Checks if df is None or empty
        if df is None or df.empty:
            self.skills = []
            return

        self.skills = []
        for index, row in df.iterrows():
            section_id = row.get("section_id", "").strip()
            title = row.get("title", "").strip()
            content = row.get("content", "").strip()
            if not title and not content:
                continue
            self.skills.append({"section_id": section_id, "title": title, "content": content})

    #Loads current skill section into the UI
    def current_section(self):
        #Failsafe if self.skills is empty
        if not self.skills:
            self.section_title.config(text="No sections available")
            self.section_text.config(state="normal")
            self.section_text.delete("1.0", tk.END)
            self.section_text.config(state="disabled")
            return

        section = self.skills[self.skill_index]
        n = self.skill_index + 1
        self.section_title.config(text=f"Section {n}: {section['title']}")
        self.section_text.config(state="normal")
        self.section_text.delete("1.0", tk.END)
        self.section_text.insert(tk.END, section["content"])
        self.section_text.config(state="disabled")

    def next_section(self):
        if self.skill_index == len(self.skills) - 1:
            messagebox.showinfo("Info", "This is the last section.")
            return
        self.skill_index += 1
        self.current_section()

    def prev_section(self):
        if self.skill_index == 0:
            messagebox.showinfo("Info", "This is the first section.")
            return
        self.skill_index -= 1
        self.current_section()