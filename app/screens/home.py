import tkinter as tk

from app.themes import APP_BG_CLR, APP_TITLE_TXT_CLR, TITLE_FONT

#Class for home screen, currently a placeholder
class HomeScreen:
    def __init__(self, app, parent):
        self.app = app
        self.parent = parent

        self.create_home_screen()

    def create_home_screen(self):
        screen = tk.Frame(self.parent, bg=APP_BG_CLR)
        screen.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.app.add_screen("home", screen)

        tk.Label(screen, text=f"Home Page", bg=APP_BG_CLR, fg=APP_TITLE_TXT_CLR, font=TITLE_FONT).pack(pady=40)