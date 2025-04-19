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


# Ejercicio 4
# Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# - Niño/a: menor de 12 años.
# - Adolescente: mayor o igual que 12 años y menor que 18 años.
# - Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# - Adulto/a: mayor o igual que 30 años.

# Primero solicitamos la edad 
edad = int(input("Ingrese su edad"))

# Comparar la edad contra las distintas categorias:
if edad < 12:
    print("Es un/a niño/a.")
elif edad < 18:
    print("Es un/a adolescente.")
elif edad < 30:
    print("Es un/a adulto/a joven.")
else:
    print("Es un/a adulto/a.")


# Ejercicio 5
# Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".

# Primero, pedimos que ingrese la contraseña.
contraseña = str(input("Ingrese una contraseña de entre 8 y 14 caracteres"))

# Evaluamos la longitud de la contraseña para ver si es correcta, e imprimimos el mensaje
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("La contraseña es correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")


# Ejercicio 6
# El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números.
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
# - Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
#   mediana es mayor que la moda.
# - Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
#   la mediana es menor que la moda.
# - Sin sesgo: cuando la media, la mediana y la moda son iguales.
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

# Importar los paquetes necesarios:
from statistics import mode, median, mean
import random

# Definir una lista de valores aleatorios de acuerdo a lo especificado:
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Definir las variables estadísticas:
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Mostrar los valores en pantalla:
print(f"La moda es {moda}, la mediana es {mediana} y la media es {media}")

# Verificar si hay sesgo:
haySesgo = not(moda == mediana == media)

# Verificar tipo de distribucion e imprimir resultados
if haySesgo:
    if (media > mediana) and (mediana > moda):
        print("Hay sesgo positivo.")
    if (media < mediana) and (mediana < moda):
        print("Hay sesgo negativo.")
else:
    print("No hay sesgo.")


# Ejercicio 7
# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

# Primero, se solicita el ingreso de un string:
frase = str(input("Ingrese una frase o palabra"))

# Se obtiene la ultima letra y se verifica si es vocal:
ultimaEsVocal = frase[-1] in "aeiouAEIOU"

# Se imprime la salida correspondiente:
if ultimaEsVocal:
    print(f"{frase}!")
else:
    print(frase)


# Ejercicio 8
# Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.

# Primero, pedimos ingresar el nombre al usuario:
nombre = str(input("Ingrese su nombre: "))

# Pedir al usuario que ingrese la opcion que prefiera:
print("Elija la opción:\n1 --> Si quiere su nombre en mayúsculas.\n2 --> Si quiere su nombre en minúsculas.\n3 --> Si quiere su nombre con la primera letra mayúscula.")
opcion = int(input("Ingrese el número de opción deceado (1-3): "))

# Imprimir el nombre de acuerdo a la opcion elegida:
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print(f"{opcion} no es una opción válida.")


# Ejercicio 9
# Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el
# resultado por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#   generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#   débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

# Ingresar la magnitud del terremoto:
magnitud = float(input("Ingrese la magnitud del terremoto en escala Richter: "))

# Clasificar de acuerdo a la magnitud
if magnitud < 3:
    categoria = "Muy leve (imperceptible)."
elif magnitud >= 3 and magnitud < 4:
    categoria = "Leve (ligeramente perceptible)."
elif magnitud >= 4 and magnitud < 5:
    categoria = "Moderado (sentido por personas, pero generalmente no causa daños)."
elif magnitud >= 5 and magnitud < 6:
    categoria = "Fuerte (puede causar daños en estructuras débiles)."
elif magnitud >= 6 and magnitud < 7:
    categoria = "Muy Fuerte (puede causar daños significativos)."
else:
    categoria = "Extremo (puede causar graves daños a gran escala)."

# Imprimir la salida:
print(f"Un sismo de magnitud {magnitud} en la escala de Richter\nes {categoria}")

