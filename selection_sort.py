import numpy as np

arr = np.random.randint(0,100,size = 10)

def selecitonSort(x):    
    for i in range(len(x)-1):
        min_index = i
        
        for j in range(i + 1 , len(x)):
            if x[j] < x[min_index]:
                min_index = j
        
        x[i], x[min_index] = x[min_index], x[i]

    return x

print(arr)
print(selecitonSort(arr.copy()))