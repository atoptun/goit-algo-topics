def binary_float_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iter_counter = 0
    bounds = [arr[0], arr[-1]]
    if x > bounds[1]:
        return (0, tuple([bounds[1], float("inf")]))
    if x < bounds[0]:
        return (0, tuple([float("-inf"), bounds[0]]))
 
    while low <= high:
        iter_counter += 1
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
            bounds[0] = arr[mid]
        elif arr[mid] > x:
            high = mid - 1
            bounds[1] = arr[mid]
        else:
            bounds[0] = bounds[1] = arr[mid]
            return (iter_counter, tuple(bounds))
 
    return (iter_counter, tuple(bounds))


def main():
    arr = [2.3, 3.2, 4.7, 10.3, 40.1]
    x = 0
    iters, bounds = binary_float_search(arr, x)
    print(f'Search: {x}. Number of iterations: {iters}. Bounds: {bounds}')


if __name__ == '__main__':
   main()