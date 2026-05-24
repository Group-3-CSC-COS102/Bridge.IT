import tkinter as tk
from app.themes import APP_BG_CLR, APP_TITLE_TXT_CLR, APP_TXT_CLR, BTN_BG_CLR, BTN_TXT_CLR, BTN_FONT
from app.widgets.tabs import create_tabs

class HomeScreen:
    def __init__(self, app, parent, app_name):
        self.app = app
        self.parent = parent
        self.app_name = app_name
        self.create_home_screen()

    def create_home_screen(self):
        screen = tk.Frame(self.parent, bg=APP_BG_CLR)
        screen.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.app.add_screen("home", screen)

        create_tabs(screen, self.app, "home")

        center = tk.Frame(screen, bg=APP_BG_CLR)
        center.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(center, text=self.app_name, bg=APP_BG_CLR,
                 fg=APP_TITLE_TXT_CLR, font=("Segoe UI", 40, "bold")).pack(pady=(0, 10))

        tk.Label(center, text="Understanding AI, One Step at a Time",
                 bg=APP_BG_CLR, fg=APP_TXT_CLR, font=("Segoe UI", 14)).pack(pady=(0, 32))

        tk.Button(
            center,
            text="Get Started →",
            font=BTN_FONT,
            bg=BTN_BG_CLR,
            fg=BTN_TXT_CLR,
            relief="flat",
            bd=0,
            padx=28,
            pady=12,
            cursor="hand2",
            command=lambda: self.app.show_screen("lessons"),
        ).pack()