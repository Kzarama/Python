# Factorial of a number in a iterative method and a recursive method
def factorialIterative(num):
    for i in range(num-1, 1, -1):
        num *= i
    return num

def factorialRecursive(num):
    if num == 0:
        return 1
    else:
        return factorialRecursive(num-1)*num

num = int(input("Enter a number:"))

print(factorialIterative(num))
print(factorialRecursive(num))