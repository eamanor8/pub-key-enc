from Crypto.Util.number import bytes_to_long, long_to_bytes
import os
import time
from binascii import hexlify

# Given keys for Task 4 and Task 5
N = int("BDDD9F7CF8B69B24810B0A0F02CE69549F5E94BAD865100F60698C13A5E190F24D8900B8E9126461110D51FA7D5C7B1E0F2DA28568D36D96BE65D9062DD2EE89", 16)
e = int("010001", 16)
d = int("6D7690B4E44FA332709384C112C51E45037CEC12AD1FD71A866353B72033E3F44FE76BCC343CB4319CCD5049AE3B52CB65102249BAF44AB834311CC908E17461", 16)

# Task 4 Q1: Signing a message directly
def sign_message(msg, N, d):
    msg_bytes = msg.encode('utf-8')
    msg_int = bytes_to_long(msg_bytes)
    signature = pow(msg_int, d, N)  # RSA signing: signature = (msg^d) mod N
    return signature

# Task 4 Q2: Verify the signature
def verify_signature(msg, signature, N, e):
    msg_bytes = msg.encode('utf-8')
    msg_int = bytes_to_long(msg_bytes)
    verified_msg_int = pow(signature, e, N)  # RSA verification: verified = (signature^e) mod N
    return msg_int == verified_msg_int

# Task 5 Q1: Sign and verify a custom message
custom_message = "Thanksgiving break is almost here!"
custom_signature = sign_message(custom_message, N, d)
print("\nCustom Message:", custom_message)
print("Custom Signature (hex):", hex(custom_signature))
is_custom_valid = verify_signature(custom_message, custom_signature, N, e)
print("Is the custom signature valid?", is_custom_valid)

# Task 5 Q2: Testing file sizes for signing
def generate_file(size_in_bytes):
    filename = ""
    filenames = ["1KB.txt", "100KB.txt", "1MB.txt", "10MB.txt"]
    file_sizes = [1024, 102400, 1048576, 10 * 1024 * 1024]
    for size in file_sizes:
        if size == size_in_bytes:
            filename = filenames[file_sizes.index(size)]
            # save file content to a file
            with open(filename, "w") as f:
                f.write("Q"*size_in_bytes)
            break

# Generate files of different sizes
file_sizes = [1024, 102400, 1048576, 10 * 1024 * 1024]
for size in file_sizes:
    generate_file(size)    

def measure_signing_time(file_content, N, d):
    msg_hex = hexlify(file_content).decode('utf-8')
    msg_int = int(msg_hex, 16)
    start_time = time.time()
    signature = pow(msg_int, d, N)
    end_time = time.time()
    return signature, end_time - start_time

# read file content from files and measure signing time
filenames = ["1KB", "100KB", "1MB", "10MB"]
print("\n\n********* Signing times for different file sizes *********")
for file in filenames:
    with open(f"{file}.txt", "rb") as f:   
        file_content = f.read()

    _, signing_time = measure_signing_time(file_content, N, d)
    print(f"Time to sign a file of size {file}: {signing_time:.8f} seconds")

print("\n\n")
