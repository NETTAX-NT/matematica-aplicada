'''Escribe un código que pida al usuario ingresar un número real y determine si el número ingresado es positivo, negativo o cero.'''
numero1=int(input("ingrese un numero "))
if numero1 >= 0 :
    print("numero positivo")
elif numero1 <= 0 :
    print("numero negativo")
elif numero1 == 0 :
    print("numero es cero")

