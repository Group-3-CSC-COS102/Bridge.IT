import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

USERS_CSV = os.path.join(DATA_DIR, "users.csv")
LESSONS_CSV = os.path.join(DATA_DIR, "lessons.csv")
TOOLS_CSV = os.path.join(DATA_DIR, "tools.csv")
SKILLS_CSV = os.path.join(DATA_DIR, "skills.csv")