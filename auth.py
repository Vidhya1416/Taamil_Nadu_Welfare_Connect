from database import get_user  # Ensure you have this import
import bcrypt

def authenticate(username, password):
    if not username or not password:
        return {"success": False, "message": "Username and Password are required"}

    user = get_user(username)
    print(f"User fetched from database: {user}")  # Debug statement

    if user and bcrypt.checkpw(password.encode('utf-8'), user[1].encode('utf-8')):  # Check hashed password
        return {"success": True, "message": f"Logged in as {username}"}
    else:
        return {"success": False, "message": "Invalid credentials"}
