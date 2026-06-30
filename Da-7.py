import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array: ", arr)

print(arr.size)
print(arr.ndim) #use to find the number of dimensions of the array
print(arr.dtype) #use to find the data type of the array

int_arr = arr.astype(int)  # Convert the array to integer type
print(int_arr)

print(int_arr.dtype)  # Check the data type of the converted array

