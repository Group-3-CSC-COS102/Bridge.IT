import tkinter as tk

class App:
    def __init__(self, app_name, root):
        self.root = root
        self.app_name = app_name
        self.root.title(app_name)
        self.root.state("zoomed")
        self.root.configure(bg="black")

        #This is a container-frame that will hold all the pages.
        self.container = tk.Frame(self.root, bg="black")
        self.container.pack(expand=True, fill="both")

        #This is a dictionary listing all the screens.
        self.screens = {}

    #This method will add a screen to the screens dictionary and place it in the container.
    def add_screen(self, screen_name, screen_frame):        
        self.screens[screen_name] = screen_frame

    #This method will switch to the given screen within the container.
    def switch_to_screen(self, screen_name):   
        self.screens[screen_name].tkraise()