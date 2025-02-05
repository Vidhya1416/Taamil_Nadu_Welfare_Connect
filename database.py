import mysql.connector
import bcrypt

def create_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",  # Just the hostname
            port=3306,  # Specify the port number separately
            user="root",
            password="cute",
            database="user_db"
        )
        print("Database connection successful")
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def add_user(username, password):
    conn = create_connection()
    if conn is None:
        print("Failed to connect to the database")
        return
    cursor = conn.cursor()
    try:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, hashed_password))
        conn.commit()
        print("User added successfully")
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
        cursor.execute('SELECT username, password FROM users WHERE username=%s', (username,))
        user = cursor.fetchone()
        print(f"User retrieved: {user}")  # Debug statement
        return user
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        cursor.close()
        conn.close()

# Ensure the table structure matches your requirements
conn = create_connection()
if conn:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
