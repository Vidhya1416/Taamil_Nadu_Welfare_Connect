from database import get_user
import bcrypt

def authenticate(username, password, role):
    print(f"Authenticating: Username={username}, Password={password}, Role={role}")

    if not username or not password or not role:
        return {"success": False, "message": "Username, Password, and Role are required"}

    user = get_user(username)
    print(f"User from database: {user}")

    if user is None:
        return {"success": False, "message": "Invalid credentials"}

    stored_username, stored_password, stored_role = user
    print(f"Stored username: {stored_username}, Stored password: {stored_password}, Stored role: {stored_role}")

    if stored_role.lower() != role.lower():
        print("Role mismatch")
        return {"success": False, "message": "Invalid role"}

    # Ensure consistent password comparison
    print(f"Comparing passwords: {password.encode('utf-8')} vs {stored_password.encode('utf-8')}")
    if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
        print("Password match")
        return {"success": True, "message": f"Logged in as {stored_username}"}
    else:
        print("Password mismatch")
        return {"success": False, "message": "Invalid credentials"}
