import sys
from fractions import Fraction
from decimal import Decimal

ideal_temp = 95.5
current_temp = 95.49

print(f"Ideal Temperature : {ideal_temp}")
print(f"Current Temperature : {current_temp}")
print(f"Difference in Temperature : {ideal_temp - current_temp}")
print(sys.float_info)