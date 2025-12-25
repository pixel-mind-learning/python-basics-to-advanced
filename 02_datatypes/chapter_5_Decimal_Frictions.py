import sys
from fractions import Fraction
from decimal import Decimal

ideal_temp = 95.5
current_temp = 95.49999999999

ideal_temp_dec = Decimal("95.5")
current_temp_dec = Decimal("95.49999999999")
diff_dec = ideal_temp_dec - current_temp_dec

print(f"Ideal temperature: {ideal_temp}")
print(f"Current temperature: {current_temp}")
print(f"Difference temperature: {ideal_temp - current_temp}")
print(sys.float_info)

print(f"Ideal temperature in Decimal: {ideal_temp_dec}")
print(f"Current temperature in Decimal: {current_temp_dec}")
print(f"Difference temperature in Decimal: {diff_dec}")
