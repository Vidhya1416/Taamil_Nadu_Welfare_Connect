import mysql.connector
import bcrypt

def create_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="cute",
            database="user_db"
        )
        print("Database connection successful")
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def add_user(username, password, role):
    conn = create_connection()
    if conn is None:
        print("Failed to connect to the database")
        return
    cursor = conn.cursor()
    try:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        print(f"Hashed password for {username}: {hashed_password.decode('utf-8')}")
        cursor.execute('INSERT INTO users (username, password, role) VALUES (%s, %s, %s)', (username, hashed_password.decode('utf-8'), role))
        conn.commit()
        print(f"User {username} added with role {role}")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

def get_user(username):
    conn = create_connection()
    if conn is None:
        print("Failed to connect to the database")
        return None
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT username, password, role FROM users WHERE username=%s', (username,))
        user = cursor.fetchone()
        print(f"User retrieved: {user}")
        return user
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        cursor.close()
        conn.close()

# Create the users table if it doesn't exist
conn = create_connection()
if conn:
    cursor = conn.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                role VARCHAR(50) NOT NULL
            )
        """)
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()
