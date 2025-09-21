def quicksort(arr):
    print('arr', arr)
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print('l', left, 'm', middle, 'r', right)
    return quicksort(left) + middle + quicksort(right)

numbers = [5, 3, 8, 4, 2]
# numbers = [2, 3, 4, 5, 8]
print(numbers)
numbers = quicksort(numbers)
print(numbers)
