def recurs(n, power):
    if n > 1000:
        return n
    return recurs(n**power, power)

print(f"Results: {recurs(4,2)}")