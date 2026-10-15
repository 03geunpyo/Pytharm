import math

a, b, c = 3, 4, 5
val1 = 1 / (1 + a / b + c)
print(val1)

a, b, c = 1, 1, -6
root1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
root2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
print(root1, root2)

r = 5
area = math.pi * (r ** 2)
print(area)

beta = 2.0
g = 3.2
val4 = beta * math.exp(-g)
print(val4)

x = 0
mu = 1.5
rho = 2.0
val5 = (1 / (rho * math.sqrt(2 * math.pi))) * math.exp(-((x - mu)**2) / (2 * rho**2))
print(val5)