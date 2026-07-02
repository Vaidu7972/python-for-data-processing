#np.isinifinite(array) : check for infinite values

import numpy as np
arr = np.array([1, 2, np.inf, 4, -np.inf, 6])  # Create an array with infinite values

print(np.isinf(arr))  # Check for infinite values in the array 


cleaned_arr = np.nan_to_num(arr, posinf=1000, neginf=-1000)  # Replace positive infinity with 1000 and negative infinity with -1000
print(cleaned_arr)  # Output: [   1.    2.  