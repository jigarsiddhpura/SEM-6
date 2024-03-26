import math

def find_rank(key):
    rank = 0
    for char in sorted(key):
        key = key.replace(char, str(rank), 1)
        rank += 1
    key = [int(char) for char in key]
    return key

def encrypt(plaintext, key):
    columns = len(key)
    rows = math.ceil(len(plaintext) / columns)
    key_rank = find_rank(key)
    print("Key Rank:", key_rank)
    plaintext += "X" * (rows * columns - len(plaintext))
    matrix = [list(plaintext[i: i + columns]) for i in range(0, len(plaintext), columns)]
    for row in matrix:
        print(row)
    ciphertext = ["*" for _ in range(columns)]
    j = 0
    for i in key_rank:
        ciphertext[i] = [row[j] for row in matrix]
        j += 1
    result = []
    for sublist in ciphertext:
        result.extend(sublist)
    return "".join(result)

def decrypt(ciphertext, key):
    columns = len(key)
    rows = math.ceil(len(ciphertext) / columns)
    key_rank = find_rank(key)
    ciphertext += "X" * (rows * columns - len(ciphertext))
    ciphertext_matrix = [list(ciphertext[i:i + rows]) for i in range(0, len(ciphertext), rows)]
    result = []
    for i in range(rows):
        temp = ["*"] * len(key_rank)
        count = 0
        for rank in key_rank:
            temp[count] = ciphertext_matrix[rank][i]
            count += 1
        result.extend(temp)
    return "".join(result).rstrip("X")

# Example usage
plaintext = input("Enter the plaintext: ").upper()
key = input("Enter the key: ").upper()

print(f"\nPlain text: {plaintext}\nKey: {key}\n")

ciphertext = encrypt(plaintext, key)
print(f"After encryption, Cipher Text: {ciphertext}\n")

decrypted_text = decrypt(ciphertext, key)
print(f"After decryption, Plain Text: {decrypted_text}")
