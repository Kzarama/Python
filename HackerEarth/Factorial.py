number = int(input())
def funcion(number):
    if(number == 1):
        return 1
    else:
        return number * funcion(number - 1)
print(funcion(number))