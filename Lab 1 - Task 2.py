# =====| Calculate mathematical expression |=====

import math

# Variant №10 data
a = 0.5
x = 3.4
beta = -3.35

# Calculation
Y = (1.9 * (10 ** 3) * x - math.pow(math.e, (a * x)) + math.asin(beta + x) - math.log10(x ** 2) + a) / \
    (math.pow(math.pow(a * x - 1.72, 2), (1/3)) + 4.75 * (10 ** 1.2) * (a - x) - (0.5 * (1 + math.cos(2 * (beta - x)))))

# Output of results
print('Result expression Y = {}'.format(Y))
