from hashlib import md5
import re

class PasswordError(Exception):
    """Custom exception for password validation errors."""
    pass

def validate_password(password):
    """
    Validates the password and returns its MD5 hash if valid.
    Raises PasswordError if the password is invalid.
    """
    # chequear longitud
    if len(password) < 8:
        raise PasswordError("Password must be at least 8 characters long.")
    
    # chequear si tiene mayus
    if not re.search(r'[A-Z]', password):
        raise PasswordError("Password must include at least one uppercase letter.")
    
    # chequear si tiene minus
    if not re.search(r'[a-z]', password):
        raise PasswordError("Password must include at least one lowercase letter.")
    
    # chequear si tiene numeros
    if not re.search(r'\d', password):
        raise PasswordError("Password must include at least one number.")
    
    # si cumple con todo, genera y devuelve un MD5 hash
    return md5(password.encode()).hexdigest()



try:
    result = validate_password("MyPassword1")
    print(f"Password is valid. Hash: {result}")
except PasswordError as e:
    print(f"Password is invalid: {str(e)}")