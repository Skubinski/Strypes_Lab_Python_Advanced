def vigenere_encrypt(plaintext, keyword):
    plaintext = plaintext.upper().replace(" ", "")
    keyword = keyword.upper()
    ciphertext = ""

    keyword_repeated = (keyword * ((len(plaintext) // len(keyword)) + 1))[:len(plaintext)]

    for p, k in zip(plaintext, keyword_repeated):
        shift = (ord(p) - ord('A') + ord(k) - ord('A')) % 26
        ciphertext += chr(shift + ord('A'))

    return ciphertext

