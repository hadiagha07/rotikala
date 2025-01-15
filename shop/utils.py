import random
import string

def generate_random_code():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    code = ''.join(random.choice(characters) for _ in range(6))
    return code