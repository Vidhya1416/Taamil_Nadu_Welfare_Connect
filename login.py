import tkinter as tk
from tkinter import messagebox
from auth import authenticate
from student_dashboard import show_student_dashboard  # Import the student dashboard function

def handle_login(username_entry, password_entry, error_msg, role, root, on_admin_login_callback):
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    result = authenticate(username, password, role)
    error_msg.set(result.get("message", "An error occurred"))

    if result.get("success"):
        messagebox.showinfo("Success", result["message"])
        if role.lower() == "admin":
            on_admin_login_callback(username)
        elif role.lower() == "student":
            show_student_dashboard(root)  # Update this line
        else:
            open_dashboard(role, username, root)
    else:
        error_msg.set(result.get("message", "An error occurred"))

def open_dashboard(role, username, root):
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="#FFDEAD")  # Set the background color to navajo white

    dashboard_label = tk.Label(root, text=f"{role} Dashboard", font=("Helvetica", 20), bg="#FFDEAD")
    dashboard_label.pack(pady=20)

    welcome_message = tk.Label(root, text=f"Welcome, {username}!", font=("Helvetica", 16), bg="#FFDEAD")
    welcome_message.pack(pady=10)

def show_login(role, root, back_callback, on_admin_login_callback):
    def toggle_password_visibility(entry, button):
        if entry.cget('show') == '':
            entry.config(show='*')
            button.config(text='👁️')
        else:
            entry.config(show='')
            button.config(text='🙈')

    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="#FFDEAD")  # Set the background color to navajo white

    container = tk.Frame(root, bg="#FFDEAD")
    container.pack(expand=True, fill='both')

    center_frame = tk.Frame(container, bg="#FFDEAD")
    center_frame.place(relx=0.5, rely=0.5, anchor='center')

    title_label = tk.Label(center_frame, text=f"{role} Login", font=("Helvetica", 16), bg="#FFDEAD")
    title_label.pack(pady=20)

    form_frame = tk.Frame(center_frame, bg="#FFDEAD")
    form_frame.pack(pady=10)

    username_label = tk.Label(form_frame, text="Username:", width=15, anchor='e', bg="#FFDEAD")
    username_entry = tk.Entry(form_frame, width=30)
    username_label.grid(row=0, column=0, padx=5, pady=5)
    username_entry.grid(row=0, column=1, padx=5, pady=5)

    password_label = tk.Label(form_frame, text="Password:", width=15, anchor='e', bg="#FFDEAD")
    password_entry = tk.Entry(form_frame, show="*", width=30)
    password_label.grid(row=1, column=0, padx=5, pady=5)
    password_entry.grid(row=1, column=1, padx=5, pady=5)

    toggle_password_button = tk.Button(form_frame, text="👁️", command=lambda: toggle_password_visibility(password_entry, toggle_password_button))
    toggle_password_button.grid(row=1, column=2, padx=5, pady=5)

    error_msg = tk.StringVar()
    error_label = tk.Label(center_frame, textvariable=error_msg, fg="red", bg="#FFDEAD")
    error_label.pack(pady=5)

    login_button = tk.Button(center_frame, text="Login", command=lambda: handle_login(username_entry, password_entry, error_msg, role, root, on_admin_login_callback))
    login_button.pack(pady=20)

    back_arrow = tk.Label(root, text="←", font=("Helvetica", 24), cursor="hand2", fg="blue", bg="#FFDEAD")
    back_arrow.bind("<Button-1>", lambda e: back_callback())
    back_arrow.place(x=10, y=10)
