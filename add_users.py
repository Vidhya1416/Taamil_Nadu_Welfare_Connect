from database import add_user
import bcrypt

users = [
    ("john_doe_123", "password!2"),
    ("jane_smith_456", "password#3"),
    ("alice_johnson_789", "pass4567!"),
    ("bob_brown_1011", "myp@ssword88"),
    ("charlie_davis_1213", "qwertyUI!2"),
    ("david_lee_1415", "secret!2022"),
    ("emily_clark_1617", "password$5"),
    ("frank_white_1819", "securePass!#"),
    ("grace_hall_2021", "letmein123!"),
    ("hannah_king_2223", "abcdefGHI!2"),
    ("ian_adams_2425", "superSecret90!"),
    ("jessica_wright_2627", "hunter2#pass"),
    ("kevin_baker_2829", "myS3curePwd!"),
    ("laura_anderson_3031", "s3cur1tyTest$"),
    ("michael_hill_3233", "p@$$w0rd789"),
    ("natalie_martin_3435", "opensesame#12"),
    ("oscar_thompson_3637", "TrickyPass@98"),
    ("paul_garcia_3839", "welcome1@3$"),
    ("quincy_moore_4041", "simplePass$12"),
    ("rachel_morris_4243", "loginTest098@")
]

for username, password in users:
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    add_user(username, hashed_password.decode('utf-8'))
    print(f"User {username} added with hashed password {hashed_password.decode('utf-8')}")
