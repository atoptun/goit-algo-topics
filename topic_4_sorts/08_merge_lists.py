def merge_lists(left: list, right: list):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    # while left_index < len(left):
    #     merged.append(left[left_index])
    #     left_index += 1

    merged.extend(right[right_index:])
    # while right_index < len(right):
    #     merged.append(right[right_index])
    #     right_index += 1

    return merged


def merge_k_lists(lists: list[list]):
    result = []
    if len(lists) == 0:
        return result
    
    result.extend(lists[0])
    for i in range(1, len(lists)):
        result = merge_lists(result, lists[i])
    
    return result


lists = [[1,3,5,7,9],[0,2,3,5,8,9],[1,3,4,5],[2,6,7,9]]

res = merge_k_lists(lists)
print(res)
