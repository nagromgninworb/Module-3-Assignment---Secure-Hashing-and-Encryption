This program is for Module 3: Assignment - Secure Hashing and Encryption in SDEV 245. 
It shows three different cryptography concepts in Python:

1. SHA-256 Hashing

The program hashes a user-entered string and also hashes a small sample file.
Hashing shows how we check integrity because any change to the input gives a totally different hash.

2. Substitution Cipher (Caesar Cipher)

This part shifts each lowercase letter forward by 3 to encrypt it.
Then it shifts backward to decrypt it.
This shows how basic old-style ciphers work.

3. Digital Signature Demo

This is a very simple simulation, not real cryptography.
It signs a message by hashing it and multiplying by a private key.
Verification checks the signature using the same process.
It shows the basic idea of how digital signatures prove authenticity.

How to Run:

1. Run the Python file in VS Code or terminal

2. Type any message when asked

3. The program will show:
 SHA-256 string hash
 SHA-256 file hash
 Caesar encrypted text
 Caesar decrypted text
 Digital signature
 Signature verification result
