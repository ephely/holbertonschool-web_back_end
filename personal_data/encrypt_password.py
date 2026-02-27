import bcrypt
""" Encrypting passwords
"""

def hash_password(password: str) -> bytes:
    """
    Hashes a password with a salt using bcrypt
    """
    password_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)

    return hashed_password
