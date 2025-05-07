# Public Key Encryption and Digital Signatures (RSA)

This repository contains the implementation of RSA-based public key encryption and signature tasks, completed as part of the ECE/CS 5560 lab on Public-Key Cryptography. It demonstrates practical usage of RSA for secure communication, encryption, decryption, and digital signatures using both C (with OpenSSL) and Python.

## 🔍 Overview

The lab consists of five core tasks and one extra credit task, focusing on:

- RSA key generation
- Encryption & decryption
- Digital signing & verification
- Working with large numbers
- Manual signature validation on X.509 certificates

📄 The full report describing all tasks and outputs is included: `public_key_enc_report.pdf`

## 📁 Project Structure

```
.
├── task1/                          # Task 1: Private key derivation and timing benchmarks
├── task2/                          # Task 2: Message encryption and ciphertext validation
├── task3/                          # Task 3: Decryption with known RSA key components
├── task4/                          # Task 4: Signing messages and observing signature sensitivity
├── task5/                          # Task 5: Signature verification and performance benchmarking
├── extra/                          # Extra credit: Manual verification of X.509 web certificate signature
├── extra-credit-old/              # Older version or backup of extra credit
├── imgs/                          # Screenshots of program output and certificate validation steps
├── docs/                          # Instructions and supporting notes
├── Big_number_template.c          # C template for large number arithmetic using OpenSSL
├── Big_number_template.py         # Python version for big number operations
├── print_BN_snippet.c             # Utility for printing BIGNUMs
├── snippet_convert.c              # Snippet for hex-to-decimal BIGNUM conversion
└── public_key_enc_report.pdf      # Full lab report with explanation
```

## Technologies Used

- **OpenSSL BIGNUM library (C)**
- **Python's `Crypto.Util` and `random` libraries**
- **Command-line tools**:
  - `openssl dgst`, `openssl x509`, `openssl s_client`
  - `sha256sum`, `asn1parse`
  - Standard C compilation (`gcc -lcrypto`)

## Tasks Summary

### Task 1 – RSA Key Derivation
- Compute private key `d` given `p`, `q`, and public exponent `e`
- Benchmark key generation for key sizes from 256 to 8192 bits

### Task 2 – RSA Encryption
- Encrypt the message: "Hello, this is my first RSA message!"
- Convert ASCII to hex and use `BN_hex2bn`
- Explore message size limitations and overflow behavior

### Task 3 – RSA Decryption
- Decrypt a provided ciphertext using private key `d`
- Convert the decrypted hex back to ASCII
- Demonstrate end-to-end RSA usage with custom keys

### Task 4 – Message Signing
- Directly sign a message (not its hash) using RSA
- Demonstrate that even a minor change in the message breaks signature verification

### Task 5 – Signature Verification
- Validate a previously signed message
- Measure signing time for messages from 1KB to 10MB
- Discuss impact of key and message sizes

### Extra Credit – X.509 Certificate Signature Verification
- Download and parse a real X.509 certificate
- Extract public key (e, n), certificate body, and signature
- Manually verify certificate signature using your own code

## Report

The full lab write-up with explanations, screenshots, code snippets, and verification steps is included in:

📘 `public_key_enc_report.pdf`

It documents:
- Mathematical background and expected outputs
- Time measurements and performance implications
- Challenges in parsing and verifying real-world web certificates

## 📚 Credit

- Lab based on materials from **ECE/CS 5560: Fundamentals of Information Security**
- RSA implementation and manual verification guided by **SEED Labs** by Dr. Wenliang Du: https://seedsecuritylabs.org
