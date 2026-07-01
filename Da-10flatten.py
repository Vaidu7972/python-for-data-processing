""" 
.ravel() -> view
.flatten() -> copy
"""
import numpy as np
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d.ravel())  # Flatten the 2D array into a 1D array (view)
print(arr_2d.flatten())  # Flatten the 2D array into a 1D array (copy)


"""
indexing slicing 
    boolean masking 
    array shape 
    ravel , flatten
    """

#advance numpy 
""" 
np.insert(array , index , value , axis=None) # Insert values into an array at specified indices   
     array- original array 
     index- index or indices before which values are inserted
     value- values to be inserted
     axis- axis along which to insert values. If None, the array is flattened before insertion.
     axis=0, row wise 
     1 column wise
        
"""

import  numpy as np
arr = np.array([10,20,30,40,50,60])
print(arr)
new_arr = np.insert(arr, 2, 25)  # Insert 25 at index 2
print(new_arr)


new_arr = np.insert(arr, [1,3], [15,35])  # Insert 15 at index 1 and 35 at index 3
print(new_arr)

