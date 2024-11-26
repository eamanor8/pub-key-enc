from Crypto.Util.number import bytes_to_long, long_to_bytes

# Given keys for Task 4
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

# Original message and signing
original_message = "This is a contract for $20,000"
signature = sign_message(original_message, N, d)
print("Original Message:", original_message)
print("Signature (hex):", hex(signature))

# Verify the original signature
is_valid = verify_signature(original_message, signature, N, e)
print("Is the signature valid?", is_valid)

# Task 4 Q2: Modifying the message
modified_message = "This is a contract for $20,001"
print("\nModified Message:", modified_message)

# Verify the original signature against the modified message
is_valid_modified = verify_signature(modified_message, signature, N, e)
print("Is the original signature valid for the modified message?", is_valid_modified)

# Generate a new signature for the modified message
new_signature = sign_message(modified_message, N, d)
print("New Signature (hex):", hex(new_signature))

# Verify the new signature
is_valid_new = verify_signature(modified_message, new_signature, N, e)
print("Is the new signature valid for the modified message?", is_valid_new)