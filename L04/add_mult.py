def add_mult(a, b):
    return a + b, a * b

print(add_mult(10, 20))

add_mult_lambda = lambda a, b : (a + b, a * b)

print(add_mult_lambda(10, 20))