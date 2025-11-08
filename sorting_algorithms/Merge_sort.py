def merge(left, right):
    if left is None:
        left = []
    if right is None:
        right = []
    i = j = 0
    result_merge = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result_merge.append(left[i])
            i += 1
        elif left[i] == right[j]:
            result_merge.append(right[j])
            result_merge.append(left[i])
            i += 1
            j += 1
        else:
            result_merge.append(right[j])
            j += 1

    result_merge.extend(left[i:])
    result_merge.extend(right[j:])

    return result_merge


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])

    return merge(left_half, right_half)
