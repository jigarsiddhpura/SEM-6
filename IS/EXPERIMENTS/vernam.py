def generate_key(plain_text, key):
    key_list = list(key)
    if len(plain_text) == len(key_list):
        return "".join(key_list)
    else:
        for i in range(len(plain_text) - len(key_list)):
            key_list.append(key_list[i % len(plain_text)])
        return "".join(key_list)

def encrypt(plain_text, key):
    cipher_text = []
    for i in range(len(plain_text)):
        x = (ord(plain_text[i]) - 65) ^ (ord(key[i]) - 65)
        x += ord("A")
        cipher_text.append(chr(x))
    return "".join(cipher_text)

def decrypt(cipher_text, key):
    decrypted_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - 65) ^ (ord(key[i]) - 65)
        x += ord("A")
        decrypted_text.append(chr(x))
    return "".join(decrypted_text)

plaintext = input("Enter the plaintext : ").upper()  
key = input("Enter the key : ").upper()  

print(f"Plain Text: {plaintext}\nKey: {key}\n")

key = generate_key(plaintext, key)
print("Encrypted cipher text is:", encrypt(plaintext, key))

ciphered_text = encrypt(plaintext, key)
print("Decrypted text is:", decrypt(ciphered_text, key))
