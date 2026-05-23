import os
from tkinter import messagebox
import pandas as pd

from app.directories import LESSONS_CSV


def ensure_lessons_csv():
    if not os.path.exists(LESSONS_CSV):
        messagebox.showerror("Error", f"Lessons data file not found")
        return False
    return True


def load_lessons():
    if not ensure_lessons_csv():
        return None
    return pd.read_csv(LESSONS_CSV, dtype=str)