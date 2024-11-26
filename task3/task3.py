from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.PublicKey import RSA

# Task 3: Given keys for decryption
N = int("BDDD9F7CF8B69B24810B0A0F02CE69549F5E94BAD865100F60698C13A5E190F24D8900B8E9126461110D51FA7D5C7B1E0F2DA28568D36D96BE65D9062DD2EE89", 16)
e = int("010001", 16)
d = int("6D7690B4E44FA332709384C112C51E45037CEC12AD1FD71A866353B72033E3F44FE76BCC343CB4319CCD5049AE3B52CB65102249BAF44AB834311CC908E17461", 16)
ciphertext = int("35B8BC929DD26C75A17CDA4772FB9E6A0682ED019EE806D1507AFC064D4955BE031EACE40DD3B9F9421511EC0AF6600510E93E0C3D6F2270FF9A879C132476C", 16)

# Function to decrypt a message
def decrypt_ciphertext(ciphertext, N, d):
    decrypted_int = pow(ciphertext, d, N)
    decrypted_bytes = long_to_bytes(decrypted_int)
    return decrypted_bytes.decode('utf-8')

# Task 3 Q1: Decrypt the given ciphertext
decrypted_message = decrypt_ciphertext(ciphertext, N, d)
print("Decrypted Message:", decrypted_message)

# Task 3 Q2: Generate a new RSA key pair and encrypt/decrypt a custom message
key = RSA.generate(2048)
custom_e = key.e
custom_d = key.d
custom_N = key.n
custom_message = "Everything is working as expected in this lab!"

# Encrypt the custom message
def encrypt_message(msg, N, e):
    msg_bytes = msg.encode('utf-8')
    msg_int = bytes_to_long(msg_bytes)
    ciphertext = pow(msg_int, e, N)
    return ciphertext

# Decrypt the custom message
ciphertext_custom = encrypt_message(custom_message, custom_N, custom_e)
decrypted_custom_message = decrypt_ciphertext(ciphertext_custom, custom_N, custom_d)

print("\nCustom Message:", custom_message)
print("\nCustom Ciphertext (hex):", hex(ciphertext_custom))
print("\nDecrypted Custom Message:", decrypted_custom_message)
