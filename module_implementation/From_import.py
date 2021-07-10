# importing sqrt() and factorial from the
# module math
import math
#from math import sqrt, factorial
from math import *

# if we simply do "import math", then
# math.sqrt(16) and math.factorial()
# are required.
print(math.sqrt(16))
print(sqrt(16))
print(factorial(6))

# Import built-in module random
from random import *

print(dir(random))
a = 3.4536

# using "%" to print value till 2 decimal places
print("The value of number till 2 decimal place(using %) is : ", end="")
print('%.2f' % a)


