# Broadcasting in NumPy
#mathematical operations on arrays of different shapes
prices = [100,200,300]

discount = 10  #10% discount

final_prices =  []          #empty list to store final prices

for price in prices:
    final_price =  price - (price * discount / 100)  # Apply discount 
    final_prices.append(final_price)
    
print(final_prices)  # Output: [90.0, 180.0, 270.0]


#method is right but loop takes time to execute, 
#so we can use broadcasting in numpy to perform the same operation on arrays of different shapes 
#without the need for explicit loops.

#alternative solution using NumPy broadcasting : (small and easy to read and understand)

import numpy as np

pricess = np.array([100, 200, 300])  # Convert prices to a NumPy array
discountt = 10  # 10% discount  scalar single value 

final_pricess = pricess - (pricess * discountt / 100)  # Apply discount using broadcasting
print(final_pricess)  # Output: [90. 180. 270.]



