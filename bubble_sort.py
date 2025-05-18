import numpy as np

arr = np.random.randint(0, 100, size=20)

def bubbleSort(x):
    for j in range(len(x) - 1):
        for i in range(len(x) - 1 - j):
            if x[i] > x[i+1]:
                a = x[i+1]
                x[i+1] = x[i]
                x[i] = a
    return x

print(arr)
print(bubbleSort(arr))