# У найгіршому випадку лінійний пошук має лінійну часову складність O(n) 

def linear_search(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1


def exists_in_list(arr, x):
    return linear_search(arr, x) != -1


def main ():
    numbers = [1, 3, 5, 7, 9, 11]
    print(linear_search(numbers, 7))  # Output: 3

    numbers = [1, 3, 5, 7, 9, 11]
    print(exists_in_list(numbers, 7))  # Output: True
    print(exists_in_list(numbers, 2))  # Output: False


if __name__ == '__main__':
   main()
