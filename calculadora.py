print("1. Suma")
print("2. Resta")
print('3. Multiplicacion ')
print('4. Division ')

try:
    numero =int(input("Que operacion quiere hacer "))
    numeroUno = float(input('Digite un numero '))
    numeroDos = float(input('Digite otro numero '))       
    
    if numero <= 4:
        if numero == 1:
            suma = numeroUno+numeroDos
            print(f'La suma es {suma}')
        elif numero == 2:
            resta = numeroUno-numeroDos
            print(f'La resta es {resta}')
        elif numero == 3:
            multiplicacion =numeroUno*numeroDos
            print(f'La multiplicacion es {multiplicacion}')
        elif numero == 4:
            divsion =numeroUno/numeroDos
            print(f'La division es {numero}')
        else:
            print(' NO ESTA EN LOS OPERADORES ')
    else:
            print(' Repetir')
except ValueError:
    print('Esto no es un operador')