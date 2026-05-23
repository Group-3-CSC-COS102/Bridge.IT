import tkinter as tk
from tkinter import messagebox

from app.themes import APP_BG_CLR, APP_TITLE_TXT_CLR, APP_TXT_CLR, BTN_BG_CLR, BTN_TXT_CLR, ENTRY_BG_CLR, ENTRY_TXT_CLR, TITLE_FONT
from app.storage.user import signup, login

#Class for the start screen, welcome screen, signup screen and login screen.
class AuthScreens:
    def __init__(self, app, parent, app_name):
        self.app = app
        self.parent = parent
        self.app_name = app_name

        self.create_start_screen()
        self.create_welcome_screen()
        self.create_signup_screen()
        self.create_login_screen()

    def create_start_screen(self):
        #Creates screen as a frame and fills the parent screen
        screen = tk.Frame(self.parent, bg="#020813")
        screen.place(relx=0, rely=0, relwidth=1, relheight=1)

        #Adds the screen to app.py
        self.app.add_screen("start", screen)

        #Title
        tk.Label(screen, text=f"{self.app_name}", bg="#020813", fg=APP_TITLE_TXT_CLR, font=TITLE_FONT).pack(expand=True)

    def create_welcome_screen(self):
        #Creates screen as a frame and fills the parent screen
        screen = tk.Frame(self.parent, bg=APP_BG_CLR)
        screen.place(relx=0, rely=0, relwidth=1, relheight=1)

        #adds the screen to app.py
        self.app.add_screen("welcome", screen)

        #Title
        tk.Label(screen, text=f"Welcome to {self.app_name}", bg=APP_BG_CLR, fg=APP_TITLE_TXT_CLR, font=TITLE_FONT).pack(pady=40) #pady adds vertical spacing 
        
        #Signup Button
        tk.Button(screen, text="Sign Up", bg=BTN_BG_CLR, fg=BTN_TXT_CLR, command=lambda: self.app.show_screen("signup")).pack(pady=8)

        #Login Button
        tk.Button(screen, text="Login", bg=BTN_BG_CLR, fg=BTN_TXT_CLR, command=lambda: self.app.show_screen("login")).pack(pady=8)

    def create_signup_screen(self):
        #Creates screen as a frame and fills the parent screen
        screen = tk.Frame(self.parent, bg=APP_BG_CLR)
        screen.place(relx=0, rely=0, relwidth=1, relheight=1)

        #adds the screen to app.py
        self.app.add_screen("signup", screen)

        #variables to store the user input
        self.signup_name = tk.StringVar()
        self.signup_username = tk.StringVar()
        self.signup_password = tk.StringVar()
        self.signup_c_password = tk.StringVar()

        #frame to hold the entry fields and labels
        entry_frame = tk.Frame(screen, bg=APP_BG_CLR)
        entry_frame.pack(pady=20)

        #Title
        tk.Label(entry_frame, text="Sign Up", bg=APP_BG_CLR, fg=APP_TITLE_TXT_CLR, font=TITLE_FONT).pack(pady=40)

        #Name
        tk.Label(entry_frame, text="Name", bg=APP_BG_CLR, fg=APP_TXT_CLR).pack(anchor="w")
        tk.Entry(entry_frame, textvariable=self.signup_name, bg=ENTRY_BG_CLR, fg=ENTRY_TXT_CLR, width=28).pack(pady=(0,8))

        #Username
        tk.Label(entry_frame, text="Username", bg=APP_BG_CLR, fg=APP_TXT_CLR).pack(anchor="w")
        tk.Entry(entry_frame, textvariable=self.signup_username, bg=ENTRY_BG_CLR, fg=ENTRY_TXT_CLR, width=28).pack(pady=(0,8))

        #Password
        tk.Label(entry_frame, text="Password", bg=APP_BG_CLR, fg=APP_TXT_CLR).pack(anchor="w")
        tk.Entry(entry_frame, textvariable=self.signup_password, show="*", bg=ENTRY_BG_CLR, fg=ENTRY_TXT_CLR, width=28).pack(pady=(0,8))

        #Retype Password
        tk.Label(entry_frame, text="Confirm Password", bg=APP_BG_CLR, fg=APP_TXT_CLR).pack(anchor="w")
        tk.Entry(entry_frame, textvariable=self.signup_c_password, show="*", bg=ENTRY_BG_CLR, fg=ENTRY_TXT_CLR, width=28).pack(pady=(0,8))

        #Signup Button
        tk.Button(entry_frame, text="Sign Up", bg=BTN_BG_CLR, fg=BTN_TXT_CLR, command=self.handle_signup).pack(pady=(0,8))

        #back button
        tk.Button(entry_frame, text="Back", bg=BTN_BG_CLR, fg=BTN_TXT_CLR, command=lambda: self.app.show_screen("welcome")).pack(pady=(0,8))

    def handle_signup(self):
        # Get user input values.
        name = self.signup_name.get()
        username = self.signup_username.get()
        password = self.signup_password.get()
        c_password = self.signup_c_password.get()

        # Validate inputs
        if not name or not username or not password or not c_password:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        if password != c_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        # Saves user to storage and to app.py
        status, msg, self.app.user = signup(name, username, password)
        if status:
            messagebox.showinfo("Success", msg)
            self.clear_entries(self.signup_name, self.signup_username, self.signup_password, self.signup_c_password)
            self.app.show_screen("home")
        else:
            messagebox.showerror("Error", msg)
            return

    def create_login_screen(self):
        #Creates screen as a frame and fills the parent screen
        screen = tk.Frame(self.parent, bg=APP_BG_CLR)
        screen.place(relx=0, rely=0, relwidth=1, relheight=1)

        #adds the screen to app.py
        self.app.add_screen("login", screen)

        #variables to store the user input
        self.login_username = tk.StringVar()
        self.login_password = tk.StringVar()

        #frame to hold the entry fields and labels
        entry_frame = tk.Frame(screen, bg=APP_BG_CLR)
        entry_frame.pack(pady=20)

        #Title
        tk.Label(entry_frame, text="Login", bg=APP_BG_CLR, fg=APP_TITLE_TXT_CLR, font=TITLE_FONT).pack(pady=40)

        #Username
        tk.Label(entry_frame, text="Username", bg=APP_BG_CLR, fg=APP_TXT_CLR).pack(anchor="w")
        tk.Entry(entry_frame, textvariable=self.login_username, bg=ENTRY_BG_CLR, fg=ENTRY_TXT_CLR, width=28).pack(pady=(0,8))

        #Password
        tk.Label(entry_frame, text="Password", bg=APP_BG_CLR, fg=APP_TXT_CLR).pack(anchor="w")
        tk.Entry(entry_frame, textvariable=self.login_password, show="*", bg=ENTRY_BG_CLR, fg=ENTRY_TXT_CLR, width=28).pack(pady=(0,8))

        #Login Button
        tk.Button(entry_frame, text="Login", bg=BTN_BG_CLR, fg=BTN_TXT_CLR, command=self.handle_login).pack(pady=8)

        #back button
        tk.Button(entry_frame, text="Back", bg=BTN_BG_CLR, fg=BTN_TXT_CLR, command=lambda: self.app.show_screen("welcome")).pack(pady=8)

    def handle_login(self):
        username = self.login_username.get()
        password = self.login_password.get()

        if not username or not password:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        
        #Loads user from csv and saves to storage
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