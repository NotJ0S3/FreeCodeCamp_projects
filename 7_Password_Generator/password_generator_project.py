import re  # Importing the `re` module for regex operations
import secrets  # Importing `secrets` for generating cryptographically secure random choices
import string  # Importing `string` for predefined sets of characters (letters, digits, punctuation)

def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    """
    Generate a secure password based on the specified constraints.
    
    Parameters:
        length (int): Length of the password to generate (default: 16).
        nums (int): Minimum number of numeric characters (default: 1).
        special_chars (int): Minimum number of special characters (default: 1).
        uppercase (int): Minimum number of uppercase letters (default: 1).
        lowercase (int): Minimum number of lowercase letters (default: 1).

    Returns:
        str: A randomly generated secure password satisfying the constraints.
    """

    # Define character groups for the password
    letters = string.ascii_letters  # Includes both uppercase and lowercase letters
    digits = string.digits  # Includes numeric characters: '0123456789'
    symbols = string.punctuation  # Includes special characters like '!@#$%^&*'

    # Combine all possible characters into a single string
    all_characters = letters + digits + symbols

    while True:  # Repeat until a valid password is generated
        password = ''  # Initialize an empty password

        # Build the password by randomly selecting characters
        for _ in range(length):
            password += secrets.choice(all_characters)  # Securely choose random characters

        # Define constraints as pairs of required counts and regex patterns
        constraints = [
            (nums, r'\d'),  # Check for at least `nums` numeric characters
            (special_chars, fr'[{symbols}]'),  # Check for at least `special_chars` special characters
            (uppercase, r'[A-Z]'),  # Check for at least `uppercase` uppercase letters
            (lowercase, r'[a-z]')  # Check for at least `lowercase` lowercase letters
        ]

        # Validate if the password meets all constraints
        if all(
            constraint <= len(re.findall(pattern, password))  # Ensure the count matches or exceeds the constraint
            for constraint, pattern in constraints
        ):
            break  # Exit the loop if the password meets all requirements

    return password  # Return the valid password

if __name__ == '__main__':
    # Generate a new password using the default constraints
    new_password = generate_password()
    print('Generated password:', new_password)  # Output the generated password
