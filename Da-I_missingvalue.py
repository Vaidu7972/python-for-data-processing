""" Missing values handle 
builtin function 

1. np.isnan(): check for missing values
2. np.isnan_to_null() : convert NaN values to null
3. np.isinfinite(): check for infinite values

NAN : NOT A NUMBER CHECK MISSING VALUE OR NOT TRUE FOR NON NUMERIC VALUE
"""

#np.isnan(array) : check for missing values
import numpy as np 
arr = np.array([1, 2, np.nan, 4, np.nan, 6])        #nan : not a number empty value (true for non numeric value)

print(np.isnan(arr))  # Check for missing values in the array

print(np.isnan(arr).sum())  # Count the number of missing values in the array

print(np.isnan(arr).any())  # Check if there are any missing values in the array

print(np.nan == np.nan)  # Check if NaN is equal to NaN (returns False)   
# we  cannot compare nan with nan because it is not a number

print(np.isinf(arr))  # Check for infinite values in the array (if not present returns false)

""" if there's any missing value to find it and replace the  missing value with a specific value using np.nan_to_num() function
np.nan_to_num(array , nan=(value) default - 0
value (can be any number you want to replace the missing value with)

"""  

import numpy as np
arr = np.array([1, 2, np.nan, 4, np.nan, 6])        #nan : not a number empty value (true for non numeric value)

cleaned_arr = np.nan_to_num(arr, nan=100)  # Replace NaN values with 100
print(cleaned_arr)  # Output: [  1.   2. 100.   4. 100.   6.]
