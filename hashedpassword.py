import hashlib

def hash_password(password: str) -> str:
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password
    
password = input("Enter a password: ")
hashed = hash_password(password)
print(f"The SHA-256 hashed password is: {hashed}")
print("Thank you")