import numpy as np

arr = np.array([10,20,30])

new_arr = np.append(arr, [40, 50,60])# Append values to the end of the array
print(new_arr)


""" 
np.concatenate((arr1, arr2, ...), axis=0) # Concatenate two or more arrays along a specified axis
axis 0 > vertical stacking (row-wise)   
axis 1 > horizontal stacking (column-wise) 
"""

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
new_arr = np.concatenate((arr1,arr2)) # Concatenate arr1 and arr2 along axis 0 (default)  inserts at specific position 
print(new_arr)

arr = np.array([10,20,30])
new_arr = np.append(arr,[40,50,60])           # Append values to the end of the array
print(new_arr)

