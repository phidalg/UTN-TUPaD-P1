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


## Programa principal:
# imprimir_hola_mundo()
# saludar_usuario(input("Ingrese su nombre: "))
# nombre = input("Ingrese su nombre: ")
# apellido = input("Ingrese su apellido: ")
# edad = input("Ingrese su edad: ")
# residencia = input("Ingrese su lugar de residencia: ")
# informacion_personal(nombre, apellido, edad, residencia)
# radio = int(input("Ingrese el radio del círculo: "))
# print(f"Área: {calcular_area_circulo(radio)}")
# print(f"Perímetro: {calcular_perimetro(radio)}")
# segundos = int(input("Ingrese los segundos: "))
# print(f"Horas: {segundos_a_horas(segundos)}")
# numero = int(input("Ingrese un número: "))
# tabla_multiplicar(numero)
# num1 = int(input("Ingrese el número a: "))
# num2 = int(input("Ingrese el número b: "))
# resultado = operaciones_basicas(num1, num2)
# print(f"Resultados de operaciones entre {num1} y {num2}:")
# print(f"Suma: {resultado[0]}")
# print(f"Resta: {resultado[1]}")
# print(f"Multiplicación: {resultado[2]}")
# print(f"División: {resultado[3]}")
peso = float(input("Ingrese el peso en Kg: "))
altura = float(input("Ingrese la altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"El IMC es {imc}")



