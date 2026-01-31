from database.db_connection import get_connection
import hashlib

def hash_password(password):
    """
    Docstring for hash_password
    
    :param password: Description

    hashing: alo
    """
    return hashlib.sha256(password.encode()).hexdigest()