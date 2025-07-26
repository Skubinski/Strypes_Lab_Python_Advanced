def binary_search(arr, target, left, right):
    if left > right:
        return -1  # Елементът не е намерен

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)

arr = [1, 3, 5, 7, 9, 11, 13]
target = 9

result = binary_search(arr, target, 0, len(arr) - 1)

if result != -1:
    print(f"Елементът {target} е намерен на индекс {result}")
else:
    print("Елементът не е намерен в списъка.")