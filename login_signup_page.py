# login_signup_page.py
import tkinter as tk
from utils import set_background

def show_login_signup(role, root, back_callback, show_login_callback, show_signup_callback):
    for widget in root.winfo_children():
        widget.destroy()

    set_background(root)

    title_label = tk.Label(root, text=f"{role} Login/Signup", font=("Helvetica", 16))
    title_label.pack(pady=20)

    login_button = tk.Button(root, text="Login", command=lambda: show_login_callback(role, root, back_callback))  # Call show_login
    login_button.pack(pady=10)

    if role.lower() != "admin":  # Check if the role is not admin
        signup_button = tk.Button(root, text="Signup", command=lambda: show_signup_callback(role, root, back_callback))  # Call show_signup
        signup_button.pack(pady=10)

    back_arrow = tk.Label(root, text="←", font=("Helvetica", 24), cursor="hand2", fg="blue", bg="white")
    back_arrow.bind("<Button-1>", lambda e: back_callback())
    back_arrow.place(x=10, y=10)
