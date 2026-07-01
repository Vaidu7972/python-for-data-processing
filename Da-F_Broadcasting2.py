import numpy as np


#matching dimensions of arrays for operations
#expanding single element to match the shape of the other array
#incompatible shapes for operations will raise an error

arr = np.array([100,200,300])
result = arr * 2              #numpy will multiply each element of the array by 2
print(result)  # Output: [200 400 600]

#1d array to 2d array

import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([10, 20, 30])  #1d array

result = matrix + vector  # Broadcasting: adding a 1D array to a 2D array
print(result)


""" #error 
import numpy as np

arr1 = np.array([[1, 2,3], [4, 5, 6]])    #shape (2,3)      #note that shapes incompatible cant perform 
                                                            #for this we need to reshape the array to match the shape of the other array
arr2 = np.array([1,2])      #shape (2,1)

result = arr1 + arr2  # This will raise an error due to incompatible shapes
print(result)
"""
#how to fix the error by reshaping the array to match the shape of the other array
import numpy as np

arr1 = np.array([[1, 2,3], [4, 5, 6]])    #shape (2,3)
arr2 = np.array([1,2]).reshape(-1, 1)      #shape (2,1)

result = arr1 + arr2  # This will now work due to compatible shapes
print(result)