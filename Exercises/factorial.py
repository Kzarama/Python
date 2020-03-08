def factorialInterativo(num):

    for i in range(num-1, 1, -1):

        num *= i

    return num


def factorialRecursivo(num):

    if num == 0:

        return 1

    else:

        return factorialRecursivo(num-1)*num



num = int(input("Ingrese un numero"))

print(factorialInterativo(num))
print(factorialRecursivo(num))