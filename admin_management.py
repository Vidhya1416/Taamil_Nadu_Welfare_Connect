# admin_management.py
import tkinter as tk
from tkinter import ttk
from utils import set_background
from database import get_all_users
from login import show_login  # Import the show_login function

def show_admin_management(root, back_callback):
    for widget in root.winfo_children():
        widget.destroy()

    set_background(root)

    title_label = tk.Label(root, text="Admin Dashboard", font=("Helvetica", 20), bg="white")
    title_label.pack(pady=20)

    welcome_message = tk.Label(root, text="Welcome, Admin!", font=("Helvetica", 16), bg="white")
    welcome_message.pack(pady=10)

    def show_user_data_management():
        for widget in root.winfo_children():
            widget.destroy()

        set_background(root)

        back_arrow = tk.Label(root, text="←", font=("Helvetica", 24), cursor="hand2", fg="blue", bg="white")
        back_arrow.bind("<Button-1>", lambda e: show_admin_management(root, back_callback))
        back_arrow.place(x=10, y=10)

        title_label = tk.Label(root, text="User Data Management", font=("Helvetica", 20), bg="white")
        title_label.pack(pady=20)

        # Create Treeview widget
        tree = ttk.Treeview(root, columns=("ID", "Username", "Role"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Username", text="Username")
        tree.heading("Role", text="Role")

        # Fetch user data from the database
        users = get_all_users()

        # Insert data into the Treeview
        for user in users:
            tree.insert("", tk.END, values=user)

        tree.pack(expand=True, fill="both")

    def show_transaction_management():
        for widget in root.winfo_children():
            widget.destroy()

        set_background(root)

        back_arrow = tk.Label(root, text="←", font=("Helvetica", 24), cursor="hand2", fg="blue", bg="white")
        back_arrow.bind("<Button-1>", lambda e: show_admin_management(root, back_callback))
        back_arrow.place(x=10, y=10)

        title_label = tk.Label(root, text="Transaction Process", font=("Helvetica", 20), bg="white")
        title_label.pack(pady=20)

        tk.Label(root, text="Transaction Process Placeholder").pack(pady=20)

    def show_report_details():
        for widget in root.winfo_children():
            widget.destroy()

        set_background(root)

        back_arrow = tk.Label(root, text="←", font=("Helvetica", 24), cursor="hand2", fg="blue", bg="white")
        back_arrow.bind("<Button-1>", lambda e: show_admin_management(root, back_callback))
        back_arrow.place(x=10, y=10)

        title_label = tk.Label(root, text="Report Details", font=("Helvetica", 20), bg="white")
        title_label.pack(pady=20)

        tk.Label(root, text="Report Details Placeholder").pack(pady=20)

    def show_transaction_issue_details():
        for widget in root.winfo_children():
            widget.destroy()

        set_background(root)

        back_arrow = tk.Label(root, text="←", font=("Helvetica", 24), cursor="hand2", fg="blue", bg="white")
        back_arrow.bind("<Button-1>", lambda e: show_admin_management(root, back_callback))
        back_arrow.place(x=10, y=10)

        title_label = tk.Label(root, text="Transaction Issue Details", font=("Helvetica", 20), bg="white")
        title_label.pack(pady=20)

        tk.Label(root, text="Transaction Issue Details Placeholder").pack(pady=20)

    user_data_button = tk.Button(root, text="User Data Management", command=show_user_data_management)
    user_data_button.pack(pady=10)

    transaction_button = tk.Button(root, text="Transaction Process", command=show_transaction_management)
    transaction_button.pack(pady=10)

    report_button = tk.Button(root, text="Report Details", command=show_report_details)
    report_button.pack(pady=10)

    issue_button = tk.Button(root, text="Transaction Issue Details", command=show_transaction_issue_details)
    issue_button.pack(pady=10)

    back_button = tk.Button(root, text="Back", command=lambda: show_login("Admin", root, back_callback, lambda: show_login("Admin", root, back_callback)))
    back_button.pack(pady=20)
