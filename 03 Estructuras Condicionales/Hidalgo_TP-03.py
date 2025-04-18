# Ejercicio 1
# Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”

# Primero solicitamos la edad 
edad = int(input("Ingrese su edad"))

# Chequear si es mayor de edad
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")


# Ejercicio 2
# Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”

# Primero solicitamos la nota al usuario 
nota = int(input("Ingrese su nota"))

# Chequear si esta aprobado
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# Ejercicio 3
# Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par"

# Primero solicitamos la nota al usuario e inicializamos la variable esPar como falso
n = int(input("Ingrese un número"))
esPar = False

# Verificar se es par y cambiar el valor de la variable
esPar == (0 == n % 2)

# Imprimir el mensaje correspondiente
if esPar:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")