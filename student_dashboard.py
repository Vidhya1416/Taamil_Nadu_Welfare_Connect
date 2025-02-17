import tkinter as tk
from tkinter import messagebox

# Scholarship data specifically provided by the Tamil Nadu government for students
scholarships = [
    {"name": "Tamil Nadu State Scholarship Portal (TNSSP)", "age_limit": "Varies",
     "eligibility": "Various departments"},
    {"name": "Pre-Matric Scholarship for SC Students", "age_limit": "Class 9-10",
     "eligibility": "Annual income less than INR 2.5 lakhs"},
    {"name": "Post-Matric Scholarship for SC Students", "age_limit": "Class 11-12",
     "eligibility": "Annual family income less than INR 2.5 lakhs"},
    {"name": "Pre-Matric Scholarship for Minorities", "age_limit": "Class 1-10",
     "eligibility": "Annual income less than INR 1,00,000"},
    {"name": "Post-Matric Scholarship for Minorities", "age_limit": "Class 11-12",
     "eligibility": "Annual family income less than INR 2 lakhs"},
    {"name": "Merit Cum Means Scholarship for Professional and Technical Courses", "age_limit": "UG/PG",
     "eligibility": "Family income below INR 2.5 lakhs per annum"},
    {"name": "Begum Hazrat Mahal National Scholarship", "age_limit": "Class 9-12",
     "eligibility": "Annual income less than INR 2 lakhs"},
    {"name": "Scholarship to Son and Daughter of Differently Abled Persons", "age_limit": "Class 11 to PG",
     "eligibility": "Differently abled"},
    {"name": "Scholarship for Differently Abled Students from Class 9th Onwards", "age_limit": "Class 9 to PG",
     "eligibility": "Differently abled"},
    {"name": "Central Sector Scheme of Scholarship (CSSS)", "age_limit": "UG/PG", "eligibility": "Minimum 60% marks"},
    {"name": "First Graduate Tuition Fee Concession", "age_limit": "UG", "eligibility": "First graduate in family"},
    {"name": "Tamil Nadu Educational Trust Scholarships", "age_limit": "Varies", "eligibility": "Meritorious students"},
    {"name": "Adi Dravidar and Tribal Welfare Scholarship", "age_limit": "Varies", "eligibility": "SC/ST students"},
    {"name": "Scholarship for Orphans and Children of COVID-19 Victims", "age_limit": "Varies",
     "eligibility": "Orphans and children of COVID-19 victims"},
    {"name": "Tamil Nadu Agriculture University Scholarship", "age_limit": "UG/PG",
     "eligibility": "Agriculture students"},
    {"name": "Tamil Nadu Polytechnic Scholarship", "age_limit": "Diploma", "eligibility": "Polytechnic students"},
    {"name": "Tamil Nadu MBA/MCA Scholarship", "age_limit": "PG", "eligibility": "MBA/MCA students"},
    {"name": "Tamil Nadu Engineering Scholarship", "age_limit": "UG/PG", "eligibility": "Engineering students"},
    {"name": "Tamil Nadu Arts and Science College Scholarship", "age_limit": "UG/PG",
     "eligibility": "Arts and Science students"},
    {"name": "Tamil Nadu State Board Merit Scholarship", "age_limit": "Varies",
     "eligibility": "Top scorers in State Board exams"},
]


def show_scholarship_details(root, scholarship):
    print(f"Showing details for: {scholarship['name']}")
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Scholarship Details")

    title_label = tk.Label(root, text=scholarship["name"], font=("Helvetica", 20), bg="#d5e8d4")
    title_label.pack(pady=20)

    details = f"Age Limit: {scholarship['age_limit']}\nEligibility: {scholarship['eligibility']}"
    details_label = tk.Label(root, text=details, font=("Helvetica", 16), bg="#d5e8d4")
    details_label.pack(pady=10)

    # Debugging print statement to confirm button creation
    print("Creating Apply button")

    apply_button = tk.Button(root, text="Apply for Scholarship",
                             command=lambda: handle_apply_scholarship(),  # Use a separate function
                             bg="#76a5af", fg="white")
    apply_button.pack(pady=10)

    back_button = tk.Button(root, text="Back", command=lambda: show_student_dashboard(root), bg="#cc4125", fg="white")
    back_button.pack(pady=10)


def handle_apply_scholarship():
    print("Apply button clicked")
    messagebox.showinfo("Apply Scholarship", "Application process started for the selected scholarship.")


def show_student_dashboard(root, back_callback=None):
    print("Displaying Student Dashboard")
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Student Dashboard")
    root.configure(bg="#f4cccc")

    title_label = tk.Label(root, text="Student Dashboard", font=("Helvetica", 20), bg="#f4cccc", fg="#6aa84f")
    title_label.pack(pady=20)

    instruction_label = tk.Label(root, text="Government Scholarships", font=("Helvetica", 16), bg="#f4cccc",
                                 fg="#6aa84f")
    instruction_label.pack(pady=10)

    if back_callback:
        back_arrow = tk.Label(root, text="←", font=("Helvetica", 24), cursor="hand2", fg="blue", bg="#f4cccc")
        back_arrow.bind("<Button-1>", lambda e: back_callback())
        back_arrow.place(x=10, y=10)

    # Create a canvas and a vertical scrollbar to make the list scrollable
    canvas = tk.Canvas(root, bg="#f4cccc")
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#f4cccc")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((root.winfo_width() // 2, 0), window=scrollable_frame, anchor="n",
                         width=root.winfo_width() - 20)
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    def create_scholarship_box(frame, scholarship):
        box_frame = tk.Frame(frame, bg="white", bd=2, relief="solid", padx=10, pady=10, width=canvas.winfo_width() - 50)
        box_frame.pack(pady=5, padx=10, fill="both", expand=True)

        name_label = tk.Label(box_frame, text=scholarship["name"], font=("Helvetica", 14, "bold"), bg="white",
                              anchor="center")
        name_label.pack(anchor="center", fill="x", expand=True)

        age_limit_label = tk.Label(box_frame, text=f"Age Limit: {scholarship['age_limit']}", font=("Helvetica", 12),
                                   bg="white", anchor="center")
        age_limit_label.pack(anchor="center", fill="x", expand=True)

        eligibility_label = tk.Label(box_frame, text=f"Eligibility: {scholarship['eligibility']}",
                                     font=("Helvetica", 12), bg="white", anchor="center")
        eligibility_label.pack(anchor="center", fill="x", expand=True)

        # Debugging print statement to confirm binding
        print(f"Binding click event for: {scholarship['name']}")
        # Bind click event to the entire box frame, not just individual labels
        box_frame.bind("<Button-1>", lambda e: handle_click(e, scholarship))

        # Bind the same click event to all child widgets within the box
        for widget in box_frame.winfo_children():
            widget.bind("<Button-1>", lambda e: handle_click(e, scholarship))

    def handle_click(event, scholarship):
        print(f"Scholarship clicked: {scholarship['name']}")
        show_scholarship_details(root, scholarship)

    for scholarship in scholarships:
        create_scholarship_box(scrollable_frame, scholarship)


if __name__ == "__main__":
    def previous_page():
        print("Back arrow clicked - returning to previous page")
        # Implement this function to navigate to the previous page


    root = tk.Tk()
    root.geometry("800x600")
    show_student_dashboard(root, back_callback=previous_page)
    root.mainloop()
