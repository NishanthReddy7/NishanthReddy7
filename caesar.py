def caesar_encrypt(text, shift):
    """
    Encrypts the input text using Caesar Cipher with the given shift.

    Args:
        text (str): The text to be encrypted.
        shift (int): The shift value for the Caesar Cipher.

    Returns:
        str: The encrypted text.
    """
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            encrypted_text += char
    return encrypted_text

def main():
    # Get user input
    text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value (1-25): "))

    # Encrypt the text
    encrypted_text = caesar_encrypt(text, shift)

    # Save the encrypted text to a file
    with open("encrypted_text.txt", "w") as file:
        file.write(encrypted_text)

    print("Encrypted text saved to encrypted_text.txt")

if __name__ == "__main__":
    main()