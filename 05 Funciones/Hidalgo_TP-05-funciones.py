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




## Programa principal:

imprimir_hola_mundo()
saludar_usuario(input("Ingrese su nombre: "))
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)
radio = int(input("Ingrese el radio del círculo: "))
print(f"Área: {calcular_area_circulo(radio)}")
print(f"Perímetro: {calcular_perimetro(radio)}")


