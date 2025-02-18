import tkinter as tk
from tkinter import messagebox

# Schemes data
schemes = [
    {"name": "Chief Minister’s Uzhavar Padhukappu Thittam (CMUPT)", "description": "Provides a monthly pension of ₹1,000 to old-age farmers and destitute agricultural laborers."},
    {"name": "Indira Gandhi National Old Age Pension Scheme (IGNOAPS)", "description": "Offers a pension to farmers aged 60 and above."},
    {"name": "Indira Gandhi National Widow Pension Scheme (IGNWPS)", "description": "Provides pensions to widows of farmers."},
    {"name": "Indira Gandhi National Disability Pension Scheme (IGNDPS)", "description": "Supports farmers with disabilities."},
    {"name": "Differently Abled Pension Scheme (DAPS)", "description": "Provides a pension of ₹1,500 to differently-abled individuals."},
    {"name": "DAP Destitute Widow Pension Scheme (DWPS)", "description": "Offers a pension of ₹1,200 to destitute widows."},
    {"name": "Pension to Poor Unmarried Women (UWP)", "description": "Provides a pension of ₹1,200 to unmarried poor women aged 50 years and above."},
    {"name": "Sri Lankan Refugees Pension Scheme", "description": "Offers a pension of ₹1,200 to Sri Lankan refugees."},
]

def show_scheme_details(root, scheme, back_callback=None):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Scheme Details")
    title_label = tk.Label(root, text=scheme["name"], font=("Helvetica", 20, "bold"), bg="#d5e8d4")
    title_label.pack(pady=20)

    details = f"Description: {scheme['description']}"
    details_label = tk.Label(root, text=details, font=("Helvetica", 16, "bold"), bg="#d5e8d4")
    details_label.pack(pady=10)

    apply_button = tk.Button(root, text="Apply for Scheme",
                             command=lambda: handle_apply_scheme(),
                             bg="#76a5af", fg="white")
    apply_button.pack(pady=10)

    back_button = tk.Button(root, text="Back", command=lambda: show_farmer_dashboard(root, back_callback), bg="#cc4125", fg="white")
    back_button.pack(pady=10)

def handle_apply_scheme():
    messagebox.showinfo("Apply Scheme", "Application process started for the selected scheme.")

def show_farmer_dashboard(root, back_callback=None):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Farmer Dashboard")
    root.configure(bg="#9370DB")  # Medium purple background color

    back_arrow = tk.Label(root, text="←", font=("Helvetica", 24), cursor="hand2", fg="blue", bg="#9370DB")
    if back_callback:
        back_arrow.bind("<Button-1>", lambda e: back_callback())
    back_arrow.place(x=10, y=10)

    title_label = tk.Label(root, text="Farmer Dashboard", font=("Helvetica", 20, "bold"), bg="#9370DB", fg="black")
    title_label.pack(pady=20)

    scheme_label = tk.Label(root, text="Government Schemes", font=("Helvetica", 16, "bold"), bg="#9370DB", fg="black")
    scheme_label.pack(pady=10)

    canvas = tk.Canvas(root, bg="#9370DB")
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#9370DB")

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.create_window((root.winfo_width() // 2, 0), window=scrollable_frame, anchor="n", width=root.winfo_width() - 20)
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    def create_scheme_box(frame, scheme):
        box_frame = tk.Frame(frame, bg="white", bd=2, relief="solid", padx=10, pady=10, width=canvas.winfo_width() - 50)
        box_frame.pack(pady=5, padx=10, fill="both", expand=True)

        name_label = tk.Label(box_frame, text=scheme["name"], font=("Helvetica", 14, "bold"), bg="white", anchor="center")
        name_label.pack(anchor="center", fill="x", expand=True)

        description_label = tk.Label(box_frame, text=f"Description: {scheme['description']}", font=("Helvetica", 12), bg="white", anchor="center")
        description_label.pack(anchor="center", fill="x", expand=True)

        box_frame.bind("<Button-1>", lambda e: handle_click(e, scheme))
        for widget in box_frame.winfo_children():
            widget.bind("<Button-1>", lambda e: handle_click(e, scheme))

    def handle_click(event, scheme):
        show_scheme_details(root, scheme, back_callback)

    for scheme in schemes:
        create_scheme_box(scrollable_frame, scheme)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    show_farmer_dashboard(root)
    root.mainloop()
