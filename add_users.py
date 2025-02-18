from database import add_user
import bcrypt

users = [
    # Students
    ("student_john_doe", "studentPass1!", "student"),
    ("student_jane_smith", "studentPass2@", "student"),
    ("student_alice_johnson", "studentPass3#", "student"),
    ("student_bob_brown", "studentPass4$", "student"),
    ("student_charlie_davis", "studentPass5%", "student"),
    ("student_david_lee", "studentPass6^", "student"),
    ("student_emily_clark", "studentPass7&", "student"),
    # Farmers
    ("farmer_john_doe", "farmerPass1!", "farmer"),
    ("farmer_jane_smith", "farmerPass2@", "farmer"),
    ("farmer_alice_johnson", "farmerPass3#", "farmer"),
    ("farmer_bob_brown", "farmerPass4$", "farmer"),
    ("farmer_charlie_davis", "farmerPass5%", "farmer"),
    ("farmer_david_lee", "farmerPass6^", "farmer"),
    ("farmer_emily_clark", "farmerPass7&", "farmer"),
    # Admins
    ("admin_john_doe", "adminPass1!", "admin"),
    ("admin_jane_smith", "adminPass2@", "admin"),
    ("admin_alice_johnson", "adminPass3#", "admin"),
    ("admin_bob_brown", "adminPass4$", "admin"),
    ("admin_charlie_davis", "adminPass5%", "admin"),
    ("admin_david_lee", "adminPass6^", "admin"),
    ("admin_emily_clark", "adminPass7&", "admin"),
]

for username, password, role in users:
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    add_user(username, hashed_password.decode('utf-8'), role)
    print(f"User {username} added with hashed password {hashed_password.decode('utf-8')} and role {role}")
