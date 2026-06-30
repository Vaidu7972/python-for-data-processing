import numpy as np
python_list = [1,2,3,4,5]
print(python_list)

import numpy as np
numpy_array = np.array([1,2,3,4,5])     # memory efficient and faster than python list
print(numpy_array)

matrix =  np.array([[1,2,3],[4,5,6],[7,8,9]])  # 2D array
print(matrix)

""" creating array using python list and tuple """

arr = np.array([(1,2,3,4)])
print(arr)

#default values

default_array = np.array([0, 0, 0, 0, 0])
print(default_array)

zeroes_array = np.zeros(3)  # array of zeros
print(zeroes_array)

#if i want  one
ones_array = np.ones(3)  # array of ones   ones_array is a variable
print(ones_array)

#full function 

full_array = np.full(3, 5)  # array of fives
print(full_array)

fill_array = np.full((2,2),7)   #2,2 is shape 2 rows 2 columns  and 7 is the value to fill the array
print(fill_array)

