# Ejercicio 1
# Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)


# Ejercicio 2
# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

num = int(input("Ingrese un número entero: "))
contador = 0
while num:  # El bucle se va a ejecutar mientras num no sea 0
    num = num // 10  # El operador de division entera entre 10 sirve para quitar el último digito.
    contador += 1 # Cada vez que se quita un digito a num, se incrementa el contador en 1. Así obtenemos la cantidad de digitos.
print(contador)


# Ejercicio 3
# Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese otro número entero: "))
sumatoria = 0

if num1 > num2:  # Primero tenemos que determinar cual de los dos números ingresados es más chico.
    mayor = num1
    menor = num2
else:
    mayor = num2
    menor = num1

for i in range(menor + 1, mayor): # El bucle se repite en el rango desde el menor al mayor sin incluirlos.
    sumatoria += i # Sumamos cada número dentro del rango.

print(f"La suma de los números enteros comprendidos entre {menor} y {mayor} es {sumatoria}")


# Ejercicio 4
# Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia.
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0

num = "" # Inicializamos num como una cadena bacía para garantizar la primera iteración del bucle.
suma = 0

print("Ingrese números enteros para sumarlos o 0 para detener el programa y ver el resultado.")
while num != 0: # El si codigo dentro del bucle se repite mientras el usuario no ingrese 0.
    num = int(input("Ingrese un número: ")) 
    suma += num # Sumamos el valor ingresado por el usuario.
    
print(f"La suma de todos los números ingresados es {suma}")


# Ejercicio 5
# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final,
# el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

num1 = random.randint(0, 9) # se genera el número aleatorio
num2 = "" # inicializamos como una cadena bacía para garantizar le primera iteracion del bucle.
intentos = 0

while num1 != num2: # se repite mientras el usuario no haya ingresado el número correcto.
    intentos += 1
    num2 = int(input("Ingrese un número del 0 al 9: "))
    if num1 == num2:
        print("¡Correcto!")
    else:
        print("Incorrecto, intente nuevamente.")

print(f"Le tomó {intentos} intentos adivinar el número.")


# Ejercicio 6
# Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100, 0, -2):
    print(i)


# Ejercicio 7
# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

num = -1
sumatoria = 0

while num < 0: # Chequeamos que el usuario ingrese un número positivo. ¿Se podría chequear que sea un entero?
    num = int(input("Ingrese un número entero positivo: "))

for i in range(0, num):
    sumatoria += i

print(f"La suma de los números enteros comprendidos entre 0 y {num} es {sumatoria}")


# Ejercicio 8
# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos
# son negativos y cuántos son positivos.

positivos = 0 # Inicializamos contadores en 0
negativos = 0
pares = 0
impares = 0

for i in range(0, 100):
    num = int(input(f"Ha ingreseado {i} de 100 números, ingrese un número: ")) # Pedimos que se ingrese un número, mostrando cuanto falta porque son muchos.
    # Se hacen las validaciones para contar el tipo de número según corresponda:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if num < 0:
        negativos += 1
    else:
        positivos += 1

print(f"Ha ingresado {positivos} números positivos, {negativos} negativos, {pares} pares y {impares} impares.")


# Ejercicio 9
# Elabora un programa que permita al usuario ingresar 100 números enteros
# y luego calcule la media de esos valores.

suma = 0
media = 0

for i in range(0, 100):
    suma += int(input(f"Ha ingresado {i} de 100 números, ingrese un número: "))

if suma > 0: # Evitamos el posible error de dividir entre 0 al calcular el promedio.
    media = suma / 100

print(f"La media de los valores ingresados es {media}.")


# Ejercicio 10
# Escribe un programa que invierta el orden de los dígitos de un número ingresado
# por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = int(input("Ingrese un número: "))
num_invertido = 0

while num > 0:
    num_invertido *= 10 # Movemos el número invertido un lugar a la izquierda, para poder agregar un digito a la derecha
    num_invertido += num % 10 # Obtenemos el último digito del número ingresado y lo agregamos a la derecha del nuevo número
    num = num // 10 # Se elimina el último digito de num, ya no lo necesitamos. Listo para repetir hasta que no quede ninguno.

print(num_invertido)