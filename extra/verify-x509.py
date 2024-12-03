from Crypto.Util.number import bytes_to_long, long_to_bytes

def read_hex_file(filepath):
    with open(filepath, 'r') as file:
        hex_data = file.read()
    # Remove colons, tabs, newlines, and spaces
    return ''.join(hex_data.replace(':', '').split())    

# Read inputs from files
c0_body_hash_hex = read_hex_file('c0_body_hash.txt')

signature_hex = read_hex_file('signature.txt')
signature = int(signature_hex, 16)  # Convert signature to integer

modulus_hex = read_hex_file('modulus.txt')
modulus = int(modulus_hex, 16)  # Convert modulus to integer

exponent = 65537

#print body_hash
print("\nBody hash: \t", c0_body_hash_hex)

# Decrypted signature
decrypted_signature = pow(signature, exponent, modulus)
hex_value = hex(decrypted_signature)
print("\n\nDecrypted signature in hex: \n\n", hex_value, "\n\n")

