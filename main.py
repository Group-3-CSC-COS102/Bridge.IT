import tkinter as tk
from app.app import App

#This is the main file. DO NOT TOUCH
if __name__ == "__main__":
    root = tk.Tk()
    app = App("Bridge.IT", root)
    root.mainloop()