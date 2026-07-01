""" 
np.split()  - equally split an array into multiple sub-arrays
np.vsplit() - vertically split an array into multiple sub-arrays
np.hsplit() - horizontally split an array into multiple sub-arrays
"""

from pprint import pprint

import numpy as np
arr = np.array([10,20,30,40,50,60])

print(np.split(arr, 3))  # Split arr into 3 equal sub-arrays
print(np.vsplit(arr.reshape(2,3), 2))  # Vertically split arr into 2 equal sub-arrays
print(np.hsplit(arr.reshape(2,3), 3))  # Horizontally split arr into 3 equal sub-arrays