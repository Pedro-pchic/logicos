def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
numero =int(input('ingrese un numero '))

print(f'el factorial {numero } es {factorial(numero)}')