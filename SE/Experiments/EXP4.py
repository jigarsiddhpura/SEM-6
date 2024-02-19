import math
key = "APPLE"

# class SINGLE
def encrypt(msg: str) :
    cipher = ""

    msg_len = len(msg)
    msg_lst = list(msg)
    sorted_key : list = sorted(list(key))
    print(sorted_key)

    col = len(sorted_key)
    row = math.ceil(msg_len / col)

    fill_null = int((row * col) - msg_len) 
    msg_lst.extend("_" * fill_null)


    matrix = [msg_lst[i : i+col] for i in range(0,len(msg_lst),col)]
    print(matrix)

    k_idx = 0

    for _ in range(col):
        curr_idx = key.index(sorted_key[k_idx]) 
        k_idx += 1
        cipher += ''.join([row[curr_idx] for row in matrix])

    return cipher


def decrypt(msg: str) :
    pass

msg = "ATTACKONTI"
cipher = encrypt(msg)
print(cipher)