def merge(arr, start, mid, end):
    left = arr[start: mid + 1]
    right = arr[mid + 1:end + 1]

    l_idx, r_idx, i = 0, 0, start
    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] <= right[r_idx]:
            arr[i] = left[l_idx]
            l_idx += 1
        else:
            arr[i] = right[r_idx]
            r_idx += 1
        i += 1

    while l_idx < len(left):
        arr[i] = left[l_idx]
        l_idx += 1
        i += 1

    while r_idx < len(right):
        arr[i] = right[r_idx]
        r_idx += 1
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
