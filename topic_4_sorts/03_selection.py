def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
        print('step =', i, lst)
    return lst

numbers = [5, 3, 8, 4, 2]
# numbers = [2, 3, 4, 5, 8]
print(numbers)
selection_sort(numbers)
print(numbers)