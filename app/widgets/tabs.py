import tkinter as tk

from app.themes import APP_BG_CLR, APP_TXT_CLR, BTN_BG_CLR, BTN_TXT_CLR

def create_tabs(parent, app, active_tab):
    frame = tk.Frame(parent, bg=APP_BG_CLR)
    frame.pack(fill="x", pady=(10, 20))

    tabs = [
        ("home", "Home"),
        ("lessons", "Basics of AI"),
        ("tools", "AI Tools")
    ]

    for name, label in tabs:
        if name == active_tab:
            bg = "#ffffff"
            fg = "#000000"
        else:
            bg = APP_BG_CLR
            fg = APP_TXT_CLR

        tk.Button(
            frame, 
            text=label, 
            bg=bg, 
            fg=fg,  
            activebackground=BTN_BG_CLR,
            activeforeground=BTN_TXT_CLR,
            relief="flat",
            padx=10,
            pady=5,
            command=lambda n=name: app.show_screen(n)
        ).pack(side="left")