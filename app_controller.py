import tkinter as tk
from login_signup_page import show_login_signup
from role_selection import open_role_selection
from login import show_login, handle_login, open_dashboard
from signup import show_signup
from admin_management import show_admin_management
from student_dashboard import show_student_dashboard
from farmer_dashboard import show_farmer_dashboard

class AppController:
    def __init__(self, root):
        self.root = root

    def show_role_selection(self):
        open_role_selection(self.root, self.show_login_signup)

    def show_login_signup(self, role):
        show_login_signup(role, self.root, self.show_role_selection, self.show_login, self.show_signup)

    def show_login(self, role):
        show_login(role, self.root, self.show_role_selection, self.show_admin_management, self.show_student_dashboard, self.show_farmer_dashboard)

    def show_signup(self, role, root, back_callback):
        show_signup(role, self.root, back_callback)

    def show_admin_management(self, username):
        show_admin_management(self.root, lambda: self.show_login("Admin"))

    def show_student_dashboard(self, root):
        show_student_dashboard(self.root, back_callback=lambda: self.show_login("Student"))

    def show_farmer_dashboard(self, root):
        show_farmer_dashboard(self.root, back_callback=lambda: self.show_login("Farmer"))
