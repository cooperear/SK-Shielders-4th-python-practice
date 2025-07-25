from math_operations import math_operations

a = math_operations(85,40)
b = math_operations(5)

print(f'a lcm =  {a.operation('lcm')}')

print(f'a gcd = {a.operation("gcd")}')

print(f'b circle = {b.operation("circle")}')
print(f'b factorial = {b.operation("factorial")}')