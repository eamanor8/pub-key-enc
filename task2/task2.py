from Crypto.Util.number import bytes_to_long, long_to_bytes
from binascii import hexlify

# Given keys
N = int("EF38064573FC9B1DF7BD8415B6BFB64402E5DB284FE8CAD9A85F0785BC3E3D07A3CFCFCEE6C8B64C37966982472C36604EF8B5A4AA5178CD2758D0E443126C19", 16)
e = int("010001", 16)
d = int("DB94C484EA239C4B14C5FC41663F71D1DA0B1D715270700AFCF745D3676885E0FFEB7067C95BDADE54A62BE6066801093A5E2D3C2B98A95B9D763AF437B09795", 16)

# Function to encrypt a message
def encrypt_message(msg, N, e):
    msg_hex = hexlify(msg.encode()).decode()
    msg_int = int(msg_hex, 16)
    ciphertext = pow(msg_int, e, N)
    return ciphertext

# Function to decrypt a message
def decrypt_message(ciphertext, N, d):
    decrypted_int = pow(ciphertext, d, N)
    decrypted_hex = hex(decrypted_int)
    return decrypted_hex

# Task 2, Q1: Encrypt and decrypt the first message
msg1 = "Hello, this is my first RSA message!"
ciphertext1 = encrypt_message(msg1, N, e)
decrypted1 = decrypt_message(ciphertext1, N, d)

print("Original Message 1 (hex):", hexlify(msg1.encode()).decode())
print("Ciphertext 1 (hex):", hex(ciphertext1))
print("Decrypted Message 1 (hex):", decrypted1)

# Task 2, Q2: Encrypt and decrypt a longer message
msg2 = "This is a much longer second RSA message. I am having so much fun!"
ciphertext2 = encrypt_message(msg2, N, e)

decrypted2 = decrypt_message(ciphertext2, N, d)
print("\nOriginal Message 2 (hex):", hexlify(msg2.encode()).decode())
print("Ciphertext 2 (hex):", hex(ciphertext2))
print("Decrypted Message 2(hex):", decrypted2)

# RSA encryption is limited by the size of the modulus (N).
# If the message is too long, it exceeds the modulus, the decryption will fail.

