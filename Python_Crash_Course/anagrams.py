def are_anagrams(one, two):
    one = one.replace(" ","").lower()
    two = two.replace(" ","").lower()

    return sorted(one) == sorted(two)

print(are_anagrams("Vladimir Nabokov", "Vivian Darkbloom"))  # True
