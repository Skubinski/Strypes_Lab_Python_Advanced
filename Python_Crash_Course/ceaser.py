def ceaser_ciphere(word):
    new_word = ""
    for char in word:
        new_word += chr(ord(char) + 2)

    return new_word


print(ceaser_ciphere("asdd"))