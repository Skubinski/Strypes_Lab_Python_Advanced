def find_keys(looked_value, **kwargs):
    keys = []
    for key, value in kwargs.items():
        if value == looked_value:
            keys.append(key)
    return keys

print(find_keys(2, a=1, b=1, c=2))



