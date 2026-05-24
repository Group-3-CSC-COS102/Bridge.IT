import tkinter as tk
from tkinter import messagebox
from app.themes import (APP_BG_CLR, CARD_BG_CLR, APP_TITLE_TXT_CLR, APP_TXT_CLR,
                        BTN_BG_CLR, BTN_TXT_CLR, ENTRY_BG_CLR, ENTRY_TXT_CLR,
                        BORDER_CLR, TITLE_FONT, LABEL_FONT, BTN_FONT, MUTED_TXT_CLR)
from app.storage.user import signup, login

class AuthScreens:
    def __init__(self, app, parent, app_name):
        self.app = app
        self.parent = parent
        self.app_name = app_name
        self.create_start_screen()
        self.create_welcome_screen()
        self.create_signup_screen()
        self.create_login_screen()

    def make_button(self, parent, text, command, secondary=False):
        return tk.Button(
            parent,
            text=text,
            font=BTN_FONT,
            bg="#1A1A2E" if secondary else BTN_BG_CLR,
            fg=APP_TXT_CLR if secondary else BTN_TXT_CLR,
            activebackground=BORDER_CLR,
            activeforeground=BTN_TXT_CLR,
            relief="flat",
            bd=0,
            padx=20,
            pady=10,
            cursor="hand2",
            width=18,
            command=command,
        )

    def make_entry(self, parent, var, show=None):
        e = tk.Entry(
            parent,
            textvariable=var,
            bg=ENTRY_BG_CLR,
            fg=ENTRY_TXT_CLR,
            insertbackground=ENTRY_TXT_CLR,
            relief="flat",
            font=("Segoe UI", 11),
            width=28,
        )
        if show:
            e.config(show=show)
        return e

    def create_start_screen(self):
        screen = tk.Frame(self.parent, bg="#020813")
        screen.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.app.add_screen("start", screen)

        tk.Label(
            screen,
            text=self.app_name,
            bg="#020813",
            fg=APP_TITLE_TXT_CLR,
            font=("Segoe UI", 36, "bold"),
        ).pack(expand=True)

        tk.Label(
            screen,
            text="Understanding AI, One Step at a Time",
            bg="#020813",
            fg=MUTED_TXT_CLR,
            font=("Segoe UI", 13),
        ).pack(pady=(0, 80))

    def create_welcome_screen(self):
        screen = tk.Frame(self.parent, bg=APP_BG_CLR)
        screen.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.app.add_screen("welcome", screen)

        tk.Label(screen, text=self.app_name, bg=APP_BG_CLR,
                 fg=APP_TITLE_TXT_CLR, font=("Segoe UI", 36, "bold")).pack(pady=(80, 8))

        tk.Label(screen, text="Understanding AI, One Step at a Time",
                 bg=APP_BG_CLR, fg=APP_TXT_CLR, font=("Segoe UI", 13)).pack(pady=(0, 40))

        self.make_button(screen, "Sign Up", lambda: self.app.show_screen("signup")).pack(pady=6)
        self.make_button(screen, "Login", lambda: self.app.show_screen("login"), secondary=True).pack(pady=6)

    def create_signup_screen(self):
        screen = tk.Frame(self.parent, bg=APP_BG_CLR)
        screen.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.app.add_screen("signup", screen)

        self.signup_name       = tk.StringVar()
        self.signup_username   = tk.StringVar()
        self.signup_password   = tk.StringVar()
        self.signup_c_password = tk.StringVar()

        card = tk.Frame(screen, bg=CARD_BG_CLR, padx=40, pady=40)
        card.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(card, text="Create Account", bg=CARD_BG_CLR,
                 fg=APP_TITLE_TXT_CLR, font=TITLE_FONT).pack(pady=(0, 24))

        for label, var, show in [
            ("Name",             self.signup_name,       None),
            ("Username",         self.signup_username,   None),
            ("Password",         self.signup_password,   "*"),
            ("Confirm Password", self.signup_c_password, "*"),
        ]:
            tk.Label(card, text=label, bg=CARD_BG_CLR, fg=APP_TXT_CLR,
                     font=LABEL_FONT, anchor="w").pack(fill="x", pady=(6, 2))
            self.make_entry(card, var, show).pack(fill="x", pady=(0, 4))

        self.make_button(card, "Sign Up", self.handle_signup).pack(pady=(16, 6), fill="x")
        self.make_button(card, "Back", lambda: self.app.show_screen("welcome"), secondary=True).pack(fill="x")

    def handle_signup(self):
        name       = self.signup_name.get()
        username   = self.signup_username.get()
        password   = self.signup_password.get()
        c_password = self.signup_c_password.get()

        if not name or not username or not password or not c_password:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        if password != c_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        status, msg, self.app.user = signup(name, username, password)
        if status:
            messagebox.showinfo("Success", msg)
            self.clear_entries(self.signup_name, self.signup_username,
                               self.signup_password, self.signup_c_password)
            self.app.show_screen("home")
        else:
            messagebox.showerror("Error", msg)

    def create_login_screen(self):
        screen = tk.Frame(self.parent, bg=APP_BG_CLR)
        screen.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.app.add_screen("login", screen)

        self.login_username = tk.StringVar()
        self.login_password = tk.StringVar()

        card = tk.Frame(screen, bg=CARD_BG_CLR, padx=40, pady=40)
        card.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(card, text="Welcome Back", bg=CARD_BG_CLR,
                 fg=APP_TITLE_TXT_CLR, font=TITLE_FONT).pack(pady=(0, 24))

        for label, var, show in [
            ("Username", self.login_username, None),
            ("Password", self.login_password, "*"),
        ]:
            tk.Label(card, text=label, bg=CARD_BG_CLR, fg=APP_TXT_CLR,
                     font=LABEL_FONT, anchor="w").pack(fill="x", pady=(6, 2))
            self.make_entry(card, var, show).pack(fill="x", pady=(0, 4))

        self.make_button(card, "Login", self.handle_login).pack(pady=(16, 6), fill="x")
        self.make_button(card, "Back", lambda: self.app.show_screen("welcome"), secondary=True).pack(fill="x")

    def handle_login(self):
        username = self.login_username.get()
        password = self.login_password.get()

        if not username or not password:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        status, msg, self.app.user = login(username, password)
        if status:
            messagebox.showinfo("Success", msg)
            self.clear_entries(self.login_username, self.login_password)
            self.app.show_screen("home")
        else:
            messagebox.showerror("Error", msg)

    def clear_entries(self, *args):
        for var in args:
            var.set("")