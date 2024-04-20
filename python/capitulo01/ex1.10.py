import math

a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

# x = b +- raiz(b^2 - 4.a.c) / 2.a
delta = (b * b) - (4 * a * c)
raiz = math.sqrt(delta)

x_1 = (-b + raiz) / (2 * a)
x_2 = (-b - raiz) / (2 * a)

print(f"\nx': {x_1:.2f}")
print(f"x'': {x_2:.2f}")
