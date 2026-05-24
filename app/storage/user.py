import os
import pandas as pd

from app.directories import DATA_DIR, USERS_CSV

#Makes sure the csv exists and creates it if it doesn't
def ensure_users_csv():
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(USERS_CSV):
        df = pd.DataFrame(columns=["name", "username", "password"])
        df.to_csv(USERS_CSV, index=False)

#Gets csv
def load_users():
    ensure_users_csv()
    return pd.read_csv(USERS_CSV, dtype=str).fillna("")

#saves csv
def save_users(df):
    ensure_users_csv()
    df.to_csv(USERS_CSV, index=False)

#Saves a new user's info
def signup(name, username, password):
    users_df = load_users()
    if username in users_df["username"].values:
        return False, "Username already exists.", None

    user_row = pd.DataFrame([{"name": name, "username": username, "password": password}])
    user_dict = user_row.iloc[0].to_dict()
    users_df = pd.concat([users_df, user_row], ignore_index=True)
    save_users(users_df)
    return True, f"Welcome, {name}!", user_dict

#Gets a user's info
def login(username, password):
    users_df = load_users()
    user_row = users_df[(users_df["username"] == username) & (users_df["password"] == password)]
    if user_row.empty:
        return False, "Invalid username or password.", None
    
    user_dict = user_row.iloc[0].to_dict()

    name = user_row.iloc[0]["name"]
    return True, f"Welcome back, {name}!", user_dict