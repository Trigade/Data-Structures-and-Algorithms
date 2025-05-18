import numpy as np

arr = np.random.randint(0,100, size = 10,dtype=np.int32)

def mergeSort(x):
    if len(x) <= 1:
        return np.array(x, dtype=int)

    mid = len(x) // 2
    left = mergeSort(x[:mid])
    right = mergeSort(x[mid:])

    res = []

    i = j = 0 

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res.extend(left[i:])
    res.extend(right[j:])

    return np.array(res, dtype=int)

print(f"Arr = {arr} \nSorted array {mergeSort(arr)}")