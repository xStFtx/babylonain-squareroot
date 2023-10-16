def babylonian_sqrt(c, initial_guess=1.0, iterations=10):
    x_n = initial_guess
    for _ in range(iterations):
        x_n = 0.5 * (x_n + c / x_n)
    return x_n

print("Enter a number")
num = float(input())
result = babylonian_sqrt(num)
print("The approximated square root is", result)
