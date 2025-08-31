import math

degrees = float(input("Enter angle in degrees: "))

radians = math.radians(degrees)

print("Radians:", radians)
import math

x = float(input("Enter value of x: "))
y = 6 * x**2 + 4 * math.sin(x)

print("y =", y)
import math

def evaluate_functions(x):
    f = math.cos(2 * x)
    f_prime = -2 * math.sin(2 * x)
    f_double_prime = -4 * math.cos(2 * x)
    return f, f_prime, f_double_prime

x_value = math.pi
results = evaluate_functions(x_value)

print("f(x) =", results[0])
print("f'(x) =", results[1])
print("f''(x) =", results[2])
