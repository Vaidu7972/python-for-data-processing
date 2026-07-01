#reshaping and manipulating data using pandas
"""reshape (rows, columns) specify new shape if dimension match """

import numpy as np

arr = np.array([1,2,3,4,5,6]) 
reshaped_arr = arr.reshape(2,3)  # reshape to 2 rows and 3 columns
print(reshaped_arr)

