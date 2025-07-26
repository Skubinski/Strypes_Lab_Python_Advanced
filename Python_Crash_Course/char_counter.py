def counter(word):

    dict = {}

    for char in sorted(word):
        if char not in dict:
            dict[char] = 0
        dict[char] += 1
    return dict

print(counter('brontosaurus'))