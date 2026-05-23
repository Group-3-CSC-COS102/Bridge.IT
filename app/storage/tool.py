import os
from tkinter import messagebox
import pandas as pd

from app.directories import TOOLS_CSV

def ensure_tools_csv():
    if not os.path.exists(TOOLS_CSV):
        messagebox.showerror("Error", f"Tools data file not found")
        return False
    return True

def load_tools():
    if not ensure_tools_csv():
        return None
    return pd.read_csv(TOOLS_CSV, dtype=str)