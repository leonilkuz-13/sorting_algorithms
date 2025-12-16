def quick_sort(arr):
    arr = arr[:]

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        i, j = low - 1, high + 1
        while True:
            i += 1
            while arr[i] < pivot:
                i += 1
            j -= 1
            while arr[j] > pivot:
                j -= 1
            if i >= j:
                return j
            arr[i], arr[j] = arr[j], arr[i]

    def sort(low, high):
        if low < high:
            p = partition(low, high)
            sort(low, p)
            sort(p + 1, high)

    sort(0, len(arr) - 1)
    return arr
