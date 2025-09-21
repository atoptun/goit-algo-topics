def bubble_sort(lst):
    n = len(lst)
    for i in range(n-1):
        is_changed = False
        for j in range(0, n-i-1): 
            if lst[j] > lst[j+1] :
                lst[j], lst[j+1] = lst[j+1], lst[j] 
                is_changed = True
        print('step =',i, lst)
        if not is_changed:
            break
    return lst

numbers = [5, 3, 8, 4, 2]
numbers = [4, 3, 2, 5, 8]
print(numbers)
bubble_sort(numbers)
print(numbers)
