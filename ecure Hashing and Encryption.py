# Morgan Browning - SDEV 345
# Module 3: Secure Hashing and Encryption
# This program shows SHA-256 hashing for strings and a file, a simple substitution (Caesar), and a simple digital signature demo

import hashlib
from pathlib import Path

# SHA-256 Hashing

def hash_string(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def hash_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()

# Subsitution Cipher (Caesar)

def caesar_encrypt(text, shift):
    encrypted = ""
    for ch in text:
        if ch.isalpha() and ch.islower():
            new_pos = (ord(ch) - ord('a') + shift) % 26
            encrypted += chr(ord('a') + new_pos)
        else:
            encrypted += ch
    return encrypted

def caesar_decrypt(text, shift):
    decrypted = ""
    for ch in text:
        if ch.isalpha() and ch.islower():
            new_pos = (ord(ch) - ord('a') - shift) % 26
            decrypted += chr(ord('a') + new_pos)
        else:
            decrypted += ch
    return decrypted

# Digital Signature Demo

private_key = 7 # demo key
public_key = 3 # demo key

def sign_message(message):
    # Hash - convert to int = mulitply by private key
    hashed = int.from_bytes(hashlib.sha256(message.encode()).digest(), "big")
    signature = hashed * private_key
    return signature

def verify_signature(message, signature):
    hashed = int.from_bytes(hashlib.sha256(message.encode()).digest(), "big")
# Check if reversing sign matches og hash
    return signature // private_key == hashed

# Main Program

def main():
    message = input("Enter a message to use for the crypto demo: ")

    print("\n=== SHA-256 HASHING ===")
    print("String hash:", hash_string(message))

    demo_file = Path("sample.txt")
    demo_file.write_text("This is a sample file for hashing.\n")
    print("File hash:", hash_file(demo_file))

    print("\n=== Caesar Cipher ===")
    shift = 3
    encrypted = caesar_encrypt(message, shift)
    decrypted = caesar_decrypt(encrypted, shift)
    print("Shift used:", shift)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)

    print("\n=== Digital Signature Demo ===")
    print("Private key:", private_key)
    print("Public key:", public_key)

    signature = sign_message(message)
    print("Signature:", signature)
    print("Signature valid?:", verify_signature(message, signature))

if __name__ == "__main__":
    main()
