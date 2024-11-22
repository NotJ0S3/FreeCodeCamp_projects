# Function to verify if a card number is valid using the Luhn algorithm
def verify_card_number(card_number):
    # Initialize the sum of digits in odd positions
    sum_of_odd_digits = 0
    # Reverse the card number to facilitate processing
    card_number_reversed = card_number[::-1]
    # Extract the digits in odd positions (from the reversed card number)
    odd_digits = card_number_reversed[::2]

    # Sum all digits in odd positions
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    # Initialize the sum of digits in even positions
    sum_of_even_digits = 0
    # Extract the digits in even positions (from the reversed card number)
    even_digits = card_number_reversed[1::2]

    # Process each digit in even positions
    for digit in even_digits:
        # Multiply the digit by 2
        number = int(digit) * 2
        # If the result is greater than or equal to 10, sum its digits
        if number >= 10:
            number = (number // 10) + (number % 10)
        # Add the processed number to the sum of even digits
        sum_of_even_digits += number

    # Calculate the total sum of odd and even digit contributions
    total = sum_of_odd_digits + sum_of_even_digits
    # Return True if the total is divisible by 10, indicating a valid card number
    return total % 10 == 0

# Main function to validate a card number
def main():
    # Card number to validate (with dashes or spaces)
    card_number = '4111-1111-4555-1142'
    # Create a translation map to remove dashes and spaces
    card_translation = str.maketrans({'-': '', ' ': ''})
    # Translate the card number to remove unwanted characters
    translated_card_number = card_number.translate(card_translation)

    # Check if the card number is valid and print the result
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

# Call the main function
main()
