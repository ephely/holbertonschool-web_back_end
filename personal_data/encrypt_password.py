#!/usr/bin/env python3
""" Encrypting passwords
"""

import bcrypt


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Checks if a password matches a hashed password
    """
    password_bytes = password.encode("utf-8")

    return bcrypt.checkpw(password_bytes, hashed_password)
