# Get prime numbers p and q
p = int(input("Enter p (prime number): "))
q = int(input("Enter q (prime number): "))

# Get public exponent e that is relatively prime to (p-1)*(q-1)
e = int(input(f"Enter e (relatively prime to {(p-1)*(q-1)}): "))

# Calculate n and φ(n)
n = p * q
phi = (p - 1) * (q - 1)

# Calculate private exponent d
d = 1
while True:
    if (d * e) % phi == 1:
        break
    d += 1

# Get message length
msg_length = int(input("Enter the length of the message (in bits): "))

# Display key and message information
print(f"p: {p}, q: {q}, message bits: {msg_length}, e: {e}")
print(f"Public key: {(e, n)}\nPrivate Key: {(d, n)}\n")

# Get message data
msg_data = int(input("Enter the message data: "))
print("Message data = ", msg_data)

# Encryption
encrypted_data = (msg_data ** e) % n
print("Encrypted data = ", encrypted_data)

# Decryption
decrypted_data = (encrypted_data ** d) % n
print("Original Message Sent = ", decrypted_data)
