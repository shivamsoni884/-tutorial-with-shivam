import random
import string

# Function to generate a random password
def generate_password(length=12, use_special_chars=True, use_numbers=True, use_uppercase=True):
    # Defining the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Create the pool of characters to use
    char_pool = lowercase
    if use_uppercase:
        char_pool += uppercase
    if use_numbers:
        char_pool += digits
    if use_special_chars:
        char_pool += special_chars

    # Generating the password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    
    return password

# Main program
def main():
    print("Welcome to the Password Generator!")
    
    # Asking user for password settings
    length = int(input("Enter the desired password length (default 12): ") or 12)
    use_special_chars = input("Include special characters (e.g., @, #, $)? (yes/no): ").lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'

    # Generate and print the password
    password = generate_password(length, use_special_chars, use_numbers, use_uppercase)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
