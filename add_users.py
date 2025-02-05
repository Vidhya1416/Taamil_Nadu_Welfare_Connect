from database import add_user
import bcrypt

users = [
    ("john_doe", "password"),
    ("jane_smith", "password123"),
    ("alice_johnson", "pass4567!"),
    ("bob_brown", "myp@ssword88"),
    ("charlie_davis", "qwertyUI12"),
    ("david_lee", "secret!2022"),
    ("emily_clark", "password567"),
    ("frank_white", "securePass!@#"),
    ("grace_hall", "letmein123!"),
    ("hannah_king", "abcdefGHI12"),
    ("ian_adams", "superSecret90!"),
    ("jessica_wright", "hunter2#pass"),
    ("kevin_baker", "myS3curePwd!"),
    ("laura_anderson", "s3cur1tyTest$"),
    ("michael_hill", "p@$$w0rd789"),
    ("natalie_martin", "opensesame#12"),
    ("oscar_thompson", "TrickyPass@98"),
    ("paul_garcia", "welcome1@3$"),
    ("quincy_moore", "simplePass$12"),
    ("rachel_morris", "loginTest098@")
]

for username, password in users:
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    add_user(username, hashed_password.decode('utf-8'))
    print(f"User {username} added with hashed password {hashed_password.decode('utf-8')}")
