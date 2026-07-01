""" 
np.delete(array , index , axis=None) # Delete elements from an array at specified indices
     array- original array
flatten array before deletion if axis is None"""

import numpy as np

arr = np.array([10,20,30,40,50,60])
print(arr)
new_arr = np.delete(arr, 2)  # Delete the element at index 2
print(new_arr)

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

new_arr_2d = np.delete(arr_2d, 0, axis=0)  # Delete the 0 row
print(new_arr_2d)

