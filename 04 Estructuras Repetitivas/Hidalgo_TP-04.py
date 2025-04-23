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
while num:
    num = num // 10
    contador += 1
print(contador)


# Ejercicio 3
# Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese otro número entero: "))
sumatoria = 0

if num1 > num2:
    mayor = num1
    menor = num2
else:
    mayor = num2
    menor = num1

for i in menor, mayor:
    sumatoria += i

print(f"La suma de los números enteros comprendidos entre {menor} y {mayor} es {sumatoria}")