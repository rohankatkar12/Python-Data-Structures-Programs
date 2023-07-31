#1. Write statement to import NumPy

"""import numpy as np
a=np.array([1,2,3,4,5])
print(a)"""


#2. create an array using Numpy
"""
import numpy as np
a = np.array([10,20,30,40,50,60])
print(a)
"""

#3. create an array of 10 random integers
"""
import numpy as np

random = np.random.randint(1,20,10)
print(random)
"""


# 4. create an array of element from 10 to 20
"""
import numpy as np
a = np.arange(10,21)
print(a)

"""


# 5. create an array which contains value 5, 10 times
"""
import numpy as np
a = np.ones(10)*5
print(a)
"""

# 6. create an one dimensional array and convert it into 3*3 matrix
"""
import numpy as np
np.random.seed( )

a = np.random.randint(1,21,9).reshape(3,3)
print(a)
"""

# 7. create an array and then converts all the even numbers with 0
"""
import numpy as np
a=np.arange(1,10)
a[a%2==0]=0
print(a)
"""


# 8. create an array of size 3*3 but all elements should be between 0 and 1
"""
import numpy as np
a=np.random.rand(9).reshape(3,3)
print(a)
"""


# 9. perform following slicing
# input=[1  2  3  4
#        5  6  7  8
#        9  10 11 12
#        13 14 15 16]

# output=[6  7
#         10 11
#         14 15]
"""
import numpy as np
a=np.arange(1,17).reshape(4,4)
b=a[1:, 1:3]
print(b)
"""


#10. Conactenate 2d array horizontally and vertically
"""
import numpy as np
np.random.seed(100)
arr1=np.arange(1,10).reshape(3,3)
arr2=np.arange(10,19).reshape(3,3)

h = np.hstack((arr1,arr2))
v = np.vstack((arr1,arr2))
print(h)
print(v)
"""













