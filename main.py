import tkinter as tk
from app_controller import AppController
from database import create_connection

if __name__ == "__main__":
    conn = create_connection()
    if conn:
        print("Database connection successful")
    else:
        print("Database connection failed")
        exit()

    root = tk.Tk()
    root.title("Tamil Nadu Welfare Connect")
    root.geometry("800x600")
    app = AppController(root)
    app.show_role_selection()
    root.mainloop()
