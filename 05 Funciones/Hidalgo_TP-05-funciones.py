PI = 3.14159265359

def imprimir_hola_mundo():
    print("Hola mundo!")

def saludar_usuario(nombre):
    print(f"¡Hola {nombre}!")

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

def calcular_area_circulo(radio):
    return PI * (radio ** 2)

def calcular_perimetro(radio):
    return PI * 2 * radio

def segundos_a_horas(segundos):
    return segundos / 3600

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {i * numero}")

def operaciones_basicas(a, b):
    return (a + b, a - b, a * b, a / b)

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def celcius_a_fahrenheit(celsius):
    return (celsius * 1.8) + 32

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

def ej(num):
    print(f"\nEjercicio {num}:\n")


## Programa principal:

ej(1) # Ejercicio 1
imprimir_hola_mundo()

ej(2) # Ejercicio 2
saludar_usuario(input("Ingrese su nombre: "))

ej(3) # Ejercicio 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

ej(4) # Ejercicio 4
radio = int(input("Ingrese el radio del círculo: "))
print(f"Área: {calcular_area_circulo(radio)}")
print(f"Perímetro: {calcular_perimetro(radio)}")

ej(5) # Ejercicio 5
segundos = int(input("Ingrese los segundos: "))
print(f"Horas: {segundos_a_horas(segundos)}")

ej(6) # Ejercicio 6
numero = int(input("Ingrese un número: "))
tabla_multiplicar(numero)

ej(7) # Ejercicio 7
num1 = int(input("Ingrese el número a: "))
num2 = int(input("Ingrese el número b: "))
resultado = operaciones_basicas(num1, num2)
print(f"Resultados de operaciones entre {num1} y {num2}:")
print(f"Suma: {resultado[0]}")
print(f"Resta: {resultado[1]}")
print(f"Multiplicación: {resultado[2]}")
print(f"División: {resultado[3]}")

ej(8) # Ejercicio 8
peso = float(input("Ingrese el peso en Kg: "))
altura = float(input("Ingrese la altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"El IMC es {imc}")

ej(9) # Ejercicio 9
temperatura = int(input("Ingrese la temperatura en grados Celsius: "))
temperatura = celcius_a_fahrenheit(temperatura)
print(f"Equivale a {temperatura} grados Fahrenheit.")

ej(10) # Ejercicio 10
num1 = int(input("Ingrese el primer número para calcular el promedio: "))
num2 = int(input("Ingrese el segundo número para calcular el promedio: "))
num3 = int(input("Ingrese el tercer número para calcularel promedio: "))
print(f"El promedio entre {num1}, {num2} y {num3} es {calcular_promedio(num1, num2, num3)}")