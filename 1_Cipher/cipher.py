# Original encrypted text
text = 'mrttaqrhknsw ih puggrur'

# The custom key used for encryption and decryption
custom_key = 'happycoding'

# Function to perform the Vigenère cipher encryption/decryption
def vigenere(message, key, direction=1):
    # Initialize the index for the key
    key_index = 0
    # Define the alphabet used for the cipher
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # Initialize the final result string
    final_message = ''

    # Iterate over each character in the message
    for char in message.lower():

        # If the character is not a letter, append it directly to the result
        if not char.isalpha():
            final_message += char
        else:        
            # Find the corresponding key character using the current key index
            key_char = key[key_index % len(key)]
            # Move to the next character in the key
            key_index += 1

            # Calculate the offset based on the key character
            offset = alphabet.index(key_char)
            # Find the index of the current character in the alphabet
            index = alphabet.find(char)
            # Calculate the new index for encryption or decryption
            new_index = (index + offset * direction) % len(alphabet)
            # Append the new character to the result
            final_message += alphabet[new_index]
    
    # Return the final encrypted or decrypted message
    return final_message

# Function to encrypt a message using the Vigenère cipher
def encrypt(message, key):
    return vigenere(message, key)
    
# Function to decrypt a message using the Vigenère cipher
def decrypt(message, key):
    return vigenere(message, key, -1)

# Print the original encrypted text
print(f'\nEncrypted text: {text}')
# Print the custom key used
print(f'Key: {custom_key}')
# Decrypt the text using the custom key
decryption = decrypt(text, custom_key)
# Print the decrypted text
print(f'\nDecrypted text: {decryption}\n')
