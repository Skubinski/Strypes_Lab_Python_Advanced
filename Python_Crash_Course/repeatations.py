def check_count(list):

    dict = {}

    for word in list:
        if word not in dict:
            dict[word] = 0
        dict[word] += 1

        if dict[word] > 1:
            return "Repeated"


    return "Not Repeated"

print(check_count([1, 2, 3]))