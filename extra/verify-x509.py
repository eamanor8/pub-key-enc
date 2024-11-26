from Crypto.Util.number import bytes_to_long, long_to_bytes

def read_hex_file(filepath):
    with open(filepath, 'r') as file:
        hex_data = file.read()
    # Remove colons, tabs, newlines, and spaces
    return ''.join(hex_data.replace(':', '').split())


# Step 5: Verification of X.509 Certificate Signature
def verify_x509_certificate(body_hash, signature, modulus, exponent):
    # Compute the hash from the decrypted signature
    decrypted_signature = pow(signature, exponent, modulus)

    # Check if the decrypted signature matches the hash of the certificate body
    return body_hash == decrypted_signature

# Read inputs from files
c0_body_hash_hex = read_hex_file('c0_body_hash.txt')
c0_body_hash = int(c0_body_hash_hex, 16)  # Convert hash to integer

signature_hex = read_hex_file('signature.txt')
signature = int(signature_hex, 16)  # Convert signature to integer

modulus_hex = read_hex_file('modulus.txt')
modulus = int(modulus_hex, 16)  # Convert modulus to integer

exponent = 65537

print(f"Body Hash (int): {c0_body_hash}")
print(f"Signature (int): {signature}")
print(f"Modulus (int): {modulus}")
print(f"Exponent (int): {exponent}")

# Decrypted signature
decrypted_signature = pow(signature, exponent, modulus)
print(f"Decrypted Signature (int): {decrypted_signature}")

# Perform the check
is_valid = c0_body_hash == decrypted_signature
print("Is the X.509 certificate signature valid?", is_valid)

