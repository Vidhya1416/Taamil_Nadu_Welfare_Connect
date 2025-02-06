import tkinter as tk
from tkinter import messagebox
from utils import set_background
from auth import authenticate

def show_login(role, root):
    def handle_login():
        username = username_entry.get()
        password = password_entry.get()

        result = authenticate(username, password)

        error_msg.set(result["message"])

        if result["success"]:
            messagebox.showinfo("Success", result["message"])
            open_dashboard(role)
        else:
            error_msg.set(result["message"])

    def open_dashboard(role):
        for widget in root.winfo_children():
            widget.destroy()

        set_background(root)

        dashboard_label = tk.Label(root, text=f"{role} Dashboard", font=("Helvetica", 20))
        dashboard_label.pack(pady=20)

        welcome_message = tk.Label(root, text=f"Welcome, {username_entry.get()}!", font=("Helvetica", 16))
        welcome_message.pack(pady=10)

    def toggle_password_visibility(entry, button):
        if entry.cget('show') == '':
            entry.config(show='*')
            button.config(text='👁️')
        else:
            entry.config(show='')
            button.config(text='🙈')

    from role_selection import open_role_selection

    for widget in root.winfo_children():
        widget.destroy()

    set_background(root)

    container = tk.Frame(root)
    container.pack(expand=True, fill='both')

    center_frame = tk.Frame(container)
    center_frame.place(relx=0.5, rely=0.5, anchor='center')

    title_label = tk.Label(center_frame, text=f"{role} Login", font=("Helvetica", 16))
    title_label.pack(pady=20)

    form_frame = tk.Frame(center_frame)
    form_frame.pack(pady=10)

    username_label = tk.Label(form_frame, text="Username:", width=15, anchor='e')
    username_entry = tk.Entry(form_frame, width=30)
    username_label.grid(row=0, column=0, padx=5, pady=5)
    username_entry.grid(row=0, column=1, padx=5, pady=5)

    password_label = tk.Label(form_frame, text="Password:", width=15, anchor='e')
    password_entry = tk.Entry(form_frame, show="*", width=30)
    password_label.grid(row=1, column=0, padx=5, pady=5)
    password_entry.grid(row=1, column=1, padx=5, pady=5)

    toggle_password_button = tk.Button(form_frame, text="👁️", command=lambda: toggle_password_visibility(password_entry, toggle_password_button))
    toggle_password_button.grid(row=1, column=2, padx=5, pady=5)

    error_msg = tk.StringVar()
    error_label = tk.Label(center_frame, textvariable=error_msg, fg="red")
    error_label.pack(pady=5)

    login_button = tk.Button(center_frame, text="Login", command=handle_login)
    login_button.pack(pady=20)

    back_arrow = tk.Label(root, text="←", font=("Helvetica", 24), cursor="hand2", fg="blue", bg="white")
    back_arrow.bind("<Button-1>", lambda e: open_role_selection(root))
    back_arrow.place(x=10, y=10)
