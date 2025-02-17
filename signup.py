import tkinter as tk
from tkinter import messagebox
import re
from utils import set_background
from database import add_user, get_user
from login import show_login
from role_selection import open_role_selection

def create_account(username_entry, password_entry, confirm_password_entry, error_msg, role, root):
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    error_msg.set("")

    if not username or not password or not confirm_password:
        error_msg.set("All fields are required")
        return

    if len(username) < 8:
        error_msg.set("Username must be at least 8 characters long")
        return

    if len(password) < 8 or not re.search(r"[0-9]", password) or not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        error_msg.set("Password must be at least 8 characters long and include at least one number and one special character")
        return

    if password != confirm_password:
        error_msg.set("Passwords do not match")
        return

    existing_user = get_user(username)
    if existing_user:
        error_msg.set("Account already exists. Redirecting to login.")
        root.after(2000, lambda: show_login(role, root, open_role_selection, lambda: show_login(role, root, open_role_selection)))  # Correct this line
        return

    add_user(username, password, role)
    messagebox.showinfo("Success", f"Account successfully created for {role}")
    root.after(2000, lambda: open_dashboard(role, root, username))

def open_dashboard(role, root, username):
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="#ADD8E6")  # Set the background color to light blue

    dashboard_label = tk.Label(root, text=f"{role} Dashboard", font=("Helvetica", 20), bg="#ADD8E6")
    dashboard_label.pack(pady=20)

    welcome_message = tk.Label(root, text=f"Welcome, {username}!", font=("Helvetica", 16), bg="#ADD8E6")
    welcome_message.pack(pady=10)

def show_signup(role, root, back_callback):
    def toggle_password_visibility(entry, button):
        if entry.cget('show') == '':
            entry.config(show='*')
            button.config(text='👁️')
        else:
            entry.config(show='')
            button.config(text='🙈')

    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="#ADD8E6")  # Set the background color to light blue

    container = tk.Frame(root, bg="#ADD8E6")
    container.pack(expand=True, fill='both')

    center_frame = tk.Frame(container, bg="#ADD8E6")
    center_frame.place(relx=0.5, rely=0.5, anchor='center')

    title_label = tk.Label(center_frame, text=f"{role} Signup", font=("Helvetica", 16), bg="#ADD8E6")
    title_label.pack(pady=20)

    form_frame = tk.Frame(center_frame, bg="#ADD8E6")
    form_frame.pack(pady=10)

    username_label = tk.Label(form_frame, text="Username:", width=15, anchor='e', bg="#ADD8E6")
    username_entry = tk.Entry(form_frame, width=30)
    username_label.grid(row=0, column=0, padx=5, pady=5)
    username_entry.grid(row=0, column=1, padx=5, pady=5)

    password_label = tk.Label(form_frame, text="Password:", width=15, anchor='e', bg="#ADD8E6")
    password_entry = tk.Entry(form_frame, show="*", width=30)
    password_label.grid(row=1, column=0, padx=5, pady=5)
    password_entry.grid(row=1, column=1, padx=5, pady=5)

    toggle_password_button = tk.Button(form_frame, text="👁️", command=lambda: toggle_password_visibility(password_entry, toggle_password_button))
    toggle_password_button.grid(row=1, column=2, padx=5, pady=5)

    confirm_password_label = tk.Label(form_frame, text="Confirm Password:", width=15, anchor='e', bg="#ADD8E6")
    confirm_password_entry = tk.Entry(form_frame, show="*", width=30)
    confirm_password_label.grid(row=2, column=0, padx=5, pady=5)
    confirm_password_entry.grid(row=2, column=1, padx=5, pady=5)

    toggle_confirm_password_button = tk.Button(form_frame, text="👁️", command=lambda: toggle_password_visibility(confirm_password_entry, toggle_confirm_password_button))
    toggle_confirm_password_button.grid(row=2, column=2, padx=5, pady=5)

    error_msg = tk.StringVar()
    error_label = tk.Label(center_frame, textvariable=error_msg, fg="red", bg="#ADD8E6")
    error_label.pack(pady=5)

    signup_button = tk.Button(center_frame, text="Signup", command=lambda: create_account(username_entry, password_entry, confirm_password_entry, error_msg, role, root))
    signup_button.pack(pady=20)

    back_arrow = tk.Label(root, text="←", font=("Helvetica", 24), cursor="hand2", fg="blue", bg="#ADD8E6")
    back_arrow.bind("<Button-1>", lambda e: back_callback())
    back_arrow.place(x=10, y=10)
