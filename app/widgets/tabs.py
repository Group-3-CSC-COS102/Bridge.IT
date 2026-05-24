import tkinter as tk
from app.themes import APP_BG_CLR, BORDER_CLR, ACCENT_CLR, APP_TXT_CLR, TAB_FONT

def create_tabs(parent, app, active_tab):
    wrapper = tk.Frame(parent, bg=BORDER_CLR)
    wrapper.pack(fill="x")

    frame = tk.Frame(wrapper, bg=APP_BG_CLR)
    frame.pack(fill="x", pady=(0, 1))

    tabs = [
        ("home",    "Home"),
        ("lessons", "Basics of AI"),
        ("tools",   "AI Tools"),
        ("skills",  "AI Skills"),
        ("welcome", "Log out"),
    ]

    for name, label in tabs:
        is_active = name == active_tab

        btn = tk.Button(
            frame,
            text=label,
            font=TAB_FONT,
            bg=APP_BG_CLR,
            fg=ACCENT_CLR if is_active else APP_TXT_CLR,
            activebackground=APP_BG_CLR,
            activeforeground=ACCENT_CLR,
            relief="flat",
            bd=0,
            padx=18,
            pady=12,
            cursor="hand2",
            command=lambda n=name: app.show_screen(n),
        )
        btn.pack(side="left")

        if is_active:
            indicator = tk.Frame(btn, bg=ACCENT_CLR, height=2)
            indicator.place(relx=0, rely=1.0, relwidth=1, anchor="sw")