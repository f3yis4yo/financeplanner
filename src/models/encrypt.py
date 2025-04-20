import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

plain_text_password = "user123"
hashed = hash_password(plain_text_password)

print(f"Hashed password: {hashed}")

login_password = "user123"
stored_hashed_password = hashed

if verify_password(login_password, stored_hashed_password):
    print("Login successful!")
else:
    print("Login failed.")