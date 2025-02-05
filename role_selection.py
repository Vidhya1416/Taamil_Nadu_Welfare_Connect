import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from utils import set_background  # Import set_background from utils

def open_login_signup(role, root):
    for widget in root.winfo_children():
        widget.destroy()

    set_background(root)

    tk.Label(root, text=f"{role} Login/Signup", font=("Helvetica", 16)).pack(pady=20)

    from login import show_login  # Import inside function to avoid circular import
    from signup import show_signup  # Import inside function to avoid circular import

    tk.Button(root, text="Login", command=lambda: show_login(role, root)).pack(pady=10)
    tk.Button(root, text="Signup", command=lambda: show_signup(role, root)).pack(pady=10)
    tk.Button(root, text="Back to Role Selection", command=lambda: open_role_selection(root)).pack(pady=10)

def animate_button(button):
    current_color = button.cget("background")
    next_color = "#FFA07A" if current_color == "#87CEFA" else "#87CEFA"
    button.config(background=next_color)
    button.after(500, animate_button, button)

def open_role_selection(root):
    for widget in root.winfo_children():
        widget.destroy()

    set_background(root)

    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 12), padding=10)

    welcome_label = tk.Label(root, text="Welcome to Tamil Nadu Welfare Connect", font=("Helvetica", 24, "bold"), fg="white", bg="black", padx=20, pady=10)
    welcome_label.pack(pady=20)

    instruction_label = tk.Label(root, text="Please select your role to proceed:", font=("Helvetica", 20), fg="white", bg="black", padx=20, pady=10)
    instruction_label.pack(pady=10)

    button_frame = tk.Frame(root, bg="pink")
    button_frame.pack(expand=True, pady=10)

    def create_role_button(frame, image_path, role):
        try:
            img = Image.open(image_path)
            img = img.resize((150, 150), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)

            bordered_frame = tk.Frame(frame, bg="white", bd=4, relief="solid")
            inner_frame = tk.Frame(bordered_frame, bg="blue", bd=2)
            bordered_frame.pack(pady=10, padx=10)
            inner_frame.pack(pady=2, padx=2)

            img_label = tk.Label(inner_frame, image=photo, bg="blue")
            img_label.image = photo
            img_label.pack(pady=10)

            button = tk.Button(inner_frame, text=role, command=lambda: open_login_signup(role, root), font=("Helvetica", 12),
                               bg="#87CEFA", activebackground="#FFA07A", relief="solid", bd=2)
            button.config(borderwidth=2, relief="solid")
            button.pack(pady=10)
            animate_button(button)
        except FileNotFoundError:
            messagebox.showerror("File Not Found", f"Image file '{image_path}' not found. Please ensure the file is in the correct directory.")

    role_frames = [tk.Frame(button_frame, bg="black") for _ in range(3)]
    for role_frame in role_frames:
        role_frame.pack(side=tk.LEFT, padx=30, pady=10, expand=True)

    create_role_button(role_frames[0], "student.png", "Student")
    create_role_button(role_frames[1], "farmer.png", "Farmer")
    create_role_button(role_frames[2], "admin.png", "Admin")
