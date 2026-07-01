import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(np.sum(arr))
print(np.mean(arr))
print(np.median(arr))
print(np.min(arr))
print(np.max(arr))
print(np.std(arr))
print(np.var(arr))

#indexing
print(arr[0])  # Accessing the first element
print(arr[1:4])  # Accessing elements from index 1 to 3
print(arr[2])
print(arr[-1]) # Accessing the last element


#slicing   
""" arr[start:stop:step]  # start is inclusive, stop is exclusive, step is optional 

arr[start:end], start  to end -1

negative step -1 reverse  
"""

import numpy as np

arr = np.array([10, 20, 30, 40, 50,60])
print(arr[1:5])  # Accessing elements from index 1 to 3 with a step of 2
print(arr[1:4])  # Accessing elements from index 1 to 3
print(arr[::2])  # Accessing every second element
print(arr[::-1])  # Reversing the array 


