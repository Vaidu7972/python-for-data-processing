"""  array[index]  #1d array
     array[row, column]  #2d array
"""

import  numpy as np
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])  # Accessing the first element
print(arr[1:4])  # Accessing elements from index 1 to 3 

""" print(arr[2])  # Accessing the third element"""





#creating sequences of numbers in numpy
#arange()
#arrange(start,stop,step)

import numpy as np
arr = np.arange(1,10,2)           # start from 1 to 10 with step of 2
print(arr)

print("Data type of the array:", arr.dtype)  # to print the data type of the array

print("Shape of the array:", arr.shape)  # to print the shape of the array



#creating identity matrix in numpy
identity_matrix = np.eye(4)  # create a 3x3 identity matrix
print(identity_matrix)


"""  array[index] #"""