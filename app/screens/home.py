import tkinter as tk

from app.themes import APP_BG_CLR, APP_TITLE_TXT_CLR, APP_TXT_CLR, BTN_BG_CLR, BTN_TXT_CLR, TITLE_FONT
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

        tk.Label(screen, text=f"{self.app_name}", bg=APP_BG_CLR, fg=APP_TITLE_TXT_CLR, font=TITLE_FONT).pack(pady=40)
        tk.Label(screen, text="Understanding AI, One Step at a Time", bg=APP_BG_CLR, fg=APP_TXT_CLR, font=("Arial", 18)).pack(pady=10)

        tk.Button(screen, text="Get Started", bg=BTN_BG_CLR, fg=BTN_TXT_CLR).pack(pady=20)