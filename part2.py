def letter_frequency(text):
    #หาความถี่ของตัวอักษรลับ
    
    frequency = {}
    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
            if letter in frequency:
                frequency[letter] += 1
            else:
                frequency[letter] = 1
    
    return frequency

def decode(encrypted_text, english_frequencies):
    encrypted_frequencies = letter_frequency(encrypted_text)

    #เอาตัวอักษรมาเรียงความถี่จากมากไปน้อย

    sorted_encrypted_frequencies = sorted(
        encrypted_frequencies.items(), key=lambda x: x[1], reverse=True)
        

    #print(sorted_encrypted_frequencies)

    sorted_english_frequencies = sorted(
        english_frequencies.items(), key=lambda x: x[1], reverse=True)
    #print(sorted_english_frequencies)

    mapping = {}
    for (encrypted_letter, encrypted_freq), (english_letter, english_freq) in zip(sorted_encrypted_frequencies, sorted_english_frequencies):
        mapping[encrypted_letter] = english_letter

    decrypted_text = ''.join(mapping.get(letter, letter)
                             for letter in encrypted_text)
    
    return(decrypted_text)
    

def crack_substitution_cipher(ciphertext):
    
    english_frequencies = {'a': 79, 'b': 14, 'c': 27, 'd': 41, 'e': 122, 'f': 21, 'g': 19, 'h': 59, 'i': 68, 'j': 2, 'k': 8, 'l': 39,
                           'm': 23, 'n': 65, 'o': 72, 'p': 18, 'q': 1, 'r': 58, 's': 61, 't': 88, 'u': 27, 'v': 10, 'w': 23, 'x': 2, 'y': 19, 'z': 10}
    return decode(ciphertext, english_frequencies)
    

with open("encrypted2.txt", "r") as f:
    texts = f.read()
ciphertext = texts.lower()
plaintext = crack_substitution_cipher(ciphertext)
print(plaintext.upper())






