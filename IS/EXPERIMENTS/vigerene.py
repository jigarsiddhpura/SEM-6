plain_txt = input("Enter plaintext : ").upper()
key = input("Enter Key : ").upper()
padd_key = key

if len(plain_txt) == len(key):
    padd_key = key
else:
    for i in range(len(plain_txt) - len(key)):
        padd_key += key[i % len(key)]

print(f"\nPlain Text : {plain_txt}\nKey : {key}\nPadded Key : {padd_key}\n")
print('Encryption : ')

encrypted = ""
for i in range(len(plain_txt)):
    encrypted += chr(((ord(plain_txt[i]) + ord(padd_key[i])) % 26) + 65)

print(f"After encryption, cipher text : {encrypted}")

print('Decryption : ')

decrypted = ""
for i in range(len(plain_txt)):
    decrypted += chr(((ord(encrypted[i]) - ord(padd_key[i])) % 26) + 65)

print(f"After decryption, decrypted text : {decrypted}")
