def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
            lst[j+1] = lst[j]
            j -= 1
            print('step =', i, j, lst)
        lst[j+1] = key 
        print('step =', i, lst)
    return lst

numbers = [5, 3, 8, 4, 2]
numbers = [2, 3, 4, 5, 8]
print(numbers)
insertion_sort(numbers)
print(numbers)
