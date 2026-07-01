""" vertically stacking and horizontally stacking of arrays
vstack() row wise stacking of arrays
hstack() column wise stacking of arrays
"""

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print(np.vstack((arr1, arr2)))  # Vertically stack arr1 and arr2
print(np.hstack((arr1, arr2)))  # Horizontally stack arr1 and arr2

print(np.column_stack((arr1, arr2)))  # Column-wise stack arr1 and arr2
