try:
    n = input("ingrese un numero")
    y =1/n
    print(y)
except ZeroDivisionError:
    print('numero no se puede dividir en 0 ')

except TypeError:
    print('no encontrado un erro0')
    

def division(p):
    return 1/p
try:
    division(0)
except ArithmeticError:
    print(' plante una  expresion')