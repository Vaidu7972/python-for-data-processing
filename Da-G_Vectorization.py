#vectorization : entire array i want to add operation with using loops
# Is operated at once instead of operating each element one by one

list1 = [1,2,3]
list2 = [4,5,6]
result = [a + b for a, b in zip(list1, list2)]
print(result)  # Output: [5, 7, 9]



#by using numpy vectorization 
import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

result = arr1 + arr2  # Vectorized operation: adding two arrays
print(result)  # Output: [5 7 9]



import numpy as np

arr = np.array([10,20,30])
print(arr)  # Output: [10 20 30]

multiplied_arr = arr * 2  # Vectorized operation: multiplying each element by 2
print(multiplied_arr)  # Output: [20 40 60]