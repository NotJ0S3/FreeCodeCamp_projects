# Converts a string written in PascalCase or camelCase to snake_case
def convert_to_snake_case(pascal_or_camel_cased_string):
    # This list comprehension iterates through each character in the input string.
    # If a character is uppercase, it adds an underscore ('_') before it and converts it to lowercase.
    # If a character is not uppercase, it is added to the list as is.
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()  # Add '_' before uppercase letters and make them lowercase
        else char  # Leave lowercase characters unchanged
        for char in pascal_or_camel_cased_string
    ]

    # Joins the characters in the list into a single string and removes any leading underscore using `strip('_')`.
    # Leading underscores may occur if the original string started with an uppercase letter.
    return ''.join(snake_cased_char_list).strip('_')

# Main function to demonstrate the usage of the `convert_to_snake_case` function
def main():
    # Example string in PascalCase; will be converted to snake_case.
    pascal_string = 'IAmAPascalCasedString'

    # Convert the string to snake_case and print the result.
    print(convert_to_snake_case(pascal_string))  # Expected output: 'i_am_a_pascal_cased_string'

# Calls the `main` function to execute the program.
main()
