key = "ILOVEHACKDBQJFRZUTPNYWMSGX"
alphabet = "abcdefghijklmnopqrstuvwxyz/.*?"
key = key.lower()

def decrypt(ciphertext, key, alphabet):
    key_map = dict(zip(key, alphabet))
    plaintext = ""
    for c in ciphertext:
        if c.lower() in key_map:
            plaintext += key_map[c.lower()]
        else:
            plaintext += c
    return plaintext

with open("encrypted3.txt", "r") as f:
    ciphertext = f.read()

print(decrypt(ciphertext, key, alphabet).upper())