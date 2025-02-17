import tkinter as tk
from app_controller import AppController
from database import create_connection  # Import create_connection

if __name__ == "__main__":
    # Create the database connection if it doesn't exist.
    if create_connection():
        print("Database connection successful")
    else:
        print("Database connection failed")
        exit()

    root = tk.Tk()
    root.title("Tamil Nadu Welfare Connect")
    root.geometry("800x600")  # Adjust the window size for better view
    app = AppController(root)
    app.show_role_selection()  # Start with role selection
    root.mainloop()
