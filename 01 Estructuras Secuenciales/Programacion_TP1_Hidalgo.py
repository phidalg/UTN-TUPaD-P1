# Programacion 1 - TP 1 - Pedro Hidalgo

# Ejercicio 1

print("Hola Mundo!")


# Ejercicio 2

nombre = input("Ingrese su nombre: ")
print(f"¡Hola {nombre}!")


#3 Ejercicio 3

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar = input("Ingrese su lugar de residencia: ")
print(f"{nombre} {apellido} tiene {edad} años y es de {lugar}.")


# Ejercicio 4

radio = int(input("Ingrese el radio de un círculo: "))
pi = 3.141592
area = pi * radio * radio
perimetro = radio * 2 * pi
print("Area: ", area)
print("Perimetro: ", perimetro)


# Ejercicio 5

segundos = int(input("Ingrese los segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivale a {horas} horas.")


# Ejercicio 6

num = int(input("Ingrese un número: "))
print(f"{num} x 1 = 1")
print(f"{num} x 2 = {num * 2}")
print(f"{num} x 3 = {num * 3}")
print(f"{num} x 4 = {num * 4}")
print(f"{num} x 5 = {num * 5}")
print(f"{num} x 6 = {num * 6}")
print(f"{num} x 7 = {num * 7}")
print(f"{num} x 8 = {num * 8}")
print(f"{num} x 9 = {num * 9}")
print(f"{num} x 10 = {num * 10}")


# Ejercicio 7

print("Ingrese dos números enteros, distintos a 0: ")
a = int(input("Número A: "))
b = int(input("Número B: "))
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{b} - {a} = {b - a}")
print(f"{a} x {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{b} / {a} = {b / a}")


# Ejercicio 8

altura = int(input("Ingrese su altura en centímetros: "))
peso = int(input("Ingrese su peso en kilogramos: "))
alturaMetros = altura / 100
imc = peso / (alturaMetros * alturaMetros)
print("Su índice de masa corporal es: ", imc)


# Ejercicio 9

c = float(input("Ingrese la temperatura en grados Celsius: "))
f = c * (9 / 5) + 32
print(f"{c} grados Celsius equivale a {f} grados Fahrenheit.")


# Ejercicio 10

print("Ingrese 3 números: ")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
print(f"El promedio de los valores ingresados es {(num1 + num2 + num3) / 3}")