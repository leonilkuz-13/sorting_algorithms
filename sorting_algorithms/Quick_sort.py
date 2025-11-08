def quick_sort(arr):
    def patrittion(nums, low, high):
        pivot = nums[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while nums[i] < pivot:
                i += 1
            j -= 1
            while nums[j] > pivot:
                j -= 1
            if i >= j:
                return j
            nums[i], nums[j] = nums[j], nums[i]

    def sort(nums, low, high):
        if low < high:
            p = patrittion(nums, low, high)
            sort(nums, low, p)
            sort(nums, p + 1, high)

    sort(arr, 0, len(arr) - 1)
    return arr
