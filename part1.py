def decrypt(text, key):
    decrypted_text = ""
    for char in text:
       
        if char.isalpha():
            shift = ord(char) + key
            
            if char.isupper():
                if shift > ord('Z'):
                    shift -= 26
            else:
                if shift > ord('z'):
                    shift -= 26
            decrypted_text += chr(shift)
      
        else:
            decrypted_text += char
    return decrypted_text

with open("encrypted1.txt", "r") as f:
    text = f.read()
for key in range(1, 26):
    if (key == 7):
        decrypted_text = decrypt(text, key)
        print(f"Key: {key}\n{decrypted_text}\n")
