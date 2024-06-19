import random
import string

def generate_password_from_names(first_name, last_name, length=12, include_uppercase=True, include_digits=True, include_symbols=True):
    name = f"{first_name.lower()}{last_name.lower()}"

    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation


    random_number = ''.join(random.choices(string.digits, k=2))
   
    password = ''.join(random.choice(characters) for _ in range(length - len(name) - len(random_number)))  # Adjust length to accommodate the name and number
    password = name + random_number + password

    return password

if __name__ == "__main__":
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    password = generate_password_from_names(first_name, last_name)
    print(f"Generated Password: {password}")
