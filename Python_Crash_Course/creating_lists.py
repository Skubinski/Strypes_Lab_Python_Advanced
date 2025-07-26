def create_list(list):
    new_list = []

    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list


print(create_list([1,2,3,3,3,4]))
