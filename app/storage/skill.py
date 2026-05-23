import os
from tkinter import messagebox
import pandas as pd

from app.directories import SKILLS_CSV


def ensure_skills_csv():
    if not os.path.exists(SKILLS_CSV):
        messagebox.showerror("Error", "Skills data file not found")
        return False
    return True


def load_skills():
    if not ensure_skills_csv():
        return None
    return pd.read_csv(SKILLS_CSV, dtype=str)