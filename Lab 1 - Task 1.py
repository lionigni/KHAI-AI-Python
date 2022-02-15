# =====| Calculate the area of a triangle |=====

import math

# Variant №10 data
sideA = 11
sideB = 7
sideC = 5

# p = (a + b + c) / 2
semiP = (sideA + sideB + sideC) / 2

# S = √‾ p * (p - a) * (p - b) * (p - c)
area = math.sqrt(semiP * (semiP - sideA) * (semiP - sideB) * (semiP - sideC))
# Alternative:  area = (semiP * (semiP - sideA) * (semiP - sideB) * (semiP - sideC)) ** 0.5

# Output of results
print('The area of the triangle is {}'.format(area))
