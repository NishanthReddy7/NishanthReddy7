from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes

# Encryption
def encrypt_message(key, plaintext):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    iv = cipher.iv
    return iv, ct_bytes

# Decryption
def decrypt_message(key, iv, ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    pt = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return pt.decode()

# Example usage
key = get_random_bytes(16)  # AES key must be either 16, 24, or 32 bytes long
plaintext = "Hello, World!"

# Encrypt the message
iv, ciphertext = encrypt_message(key, plaintext)
print("Ciphertext:", ciphertext)

# Decrypt the message
decrypted_message = decrypt_message(key, iv, ciphertext)
print("Decrypted message:", decrypted_message)