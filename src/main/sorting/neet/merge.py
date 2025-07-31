def merge(arr, start, mid, end):
    left = arr[start: mid + 1]
    right = arr[mid + 1:end + 1]

    l, r, i = 0, 0, start
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            arr[i] = left[l]
            l += 1
        else:
            arr[i] = right[r]
            r += 1
        i += 1

    while l < len(left):
        arr[i] = left[l]
        l += 1
        i += 1

    while r < len(right):
        arr[i] = right[r]
        r += 1
        i += 1

    return arr


def sort(arr, start, end):
    if (end - start + 1) <= 1:
        return arr
    mid = (start + end) // 2
    sort(arr, start, mid)
    sort(arr, mid + 1, end)
    merge(arr, start, mid, end)
    return arr
