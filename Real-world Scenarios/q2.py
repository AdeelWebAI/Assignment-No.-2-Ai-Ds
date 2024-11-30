import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 to include all character types."

    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(special)
    ]
    
    all_characters = upper + lower + digits + special
    password += random.choices(all_characters, k=length - 4)

    random.shuffle(password)
    return ''.join(password)

password_length = int(input("Enter the desired password length: "))
password = generate_password(password_length)
print(f"Generated password: {password}")
