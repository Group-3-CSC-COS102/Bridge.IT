import tkinter as tk

from app.themes import APP_BG_CLR
from app.screens.auth import AuthScreens
from app.screens.home import HomeScreen

class App:
    def __init__(self, app_name, root):
        self.root = root
        self.app_name = app_name
        self.root.title(app_name)
        self.root.state("zoomed")
        self.root.configure(bg=APP_BG_CLR)
        self.user = None

        #This is a container-frame that will hold all the pages.
        self.container = tk.Frame(self.root, bg=APP_BG_CLR)
        self.container.pack(expand=True, fill="both")

        #This is a dictionary listing all the screens.
        self.screens = {}

        #App Screens get created and process starts
        AuthScreens(self, self.container, self.app_name)
        HomeScreen(self, self.container)
        self.show_screen("start")
        self.root.after(2500, lambda: self.show_screen("welcome"))

    #This method will add a screen to the screens dictionary and place it in the container.
    def add_screen(self, screen_name, screen_frame):        
        self.screens[screen_name] = screen_frame

    #This method will switch to the given screen within the container.
    def show_screen(self, screen_name):   
        self.screens[screen_name].tkraise()

    #To get the current user's information, in case we need it
    def current_user(self):
        return self.user