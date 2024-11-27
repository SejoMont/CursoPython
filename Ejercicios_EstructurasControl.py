# Ejercicios con if
print("-- Ejercicios con if --")

a = 10
b = 100

# 1. Defina una estructura de control que imprima por pantalla “Es igual a 10” si a es igual a 10 y si no
#    imprima “Es diferente de 10”.
if a == 10:
    print("Es igual a 10")
else:
    print("Es diferente de 10")

# 2. Defina una estructura de control que imprima “Todos son igual a 10” si a y b son iguales a 10; si no
#    imprima “Solo a es igual a 10” si a es igual a 10; si no imprima “B es igual a 10” si b es igual a 10; si no
#    imprima “Ninguno es igual a 10”.
if a == 10 and b == 10:
    print("Todos son igual a 10")
elif a == 10:
    print("Solo a es igual a 10")
elif b == 10:
    print("B es igual a 10")
else:
    print("Ninguno es igual a 10")

# 3. Defina una estructura de control que imprima “A y B son impares” si tanto a como b son impares; si no
#    imprima “A y B no son impares”.
if a % 2 != 0 and b % 2 != 0:
    print("A y B son impares")
else:
    print("A y B no son impares")



# Ejercicios con while
print("\n-- Ejercicios con while --")

# 1. Asigna un valor a la variable i.
print("Ejercicio 1")
i = 3
print("i: ", i)

# 2. Defina una estructura de control que solo imprima i una vez.
print("\nEjercicio 2")
while i < 1:
    print(i)
    i += 1

# 3. Defina una estructura de control que imprima i solo si el valor de i es par.
print("\nEjercicio 3")
while i < 10:
    if i % 2 == 0:
        print(i)
    i += 1  

# 4. Asigna i el valor 0. Crea una estructura de control que vaya incrementando i mientras i sea menor de 10.
#    Comprueba si el valor de i es 6 e imprime “Ejecución terminada” y finaliza el bucle.
print("\nEjercicio 4")
i = 0
while i < 10:
    print(i)
    i += 1
    if i == 6:
        print("Ejecución terminada")
        break



# Ejercicios con for
print("\n-- Ejercicios con for --")

a = ['Hello', 'World']
b = ['Python', 3.9]
c = 'HelloWorldPython'

# 1. Recorre todos los caracteres de c e imprímelos por pantalla.
print("Ejercicio 1")
for caracter in c:
    print(caracter)

# 2. Muestra todos los valores de a.
print("\nEjercicio 2")
for valor in a:
    print(valor)

# 3. Muestra cada valor de a y b mostrando cada elemento de a con el de la misma posición de b sin utilizar
#    los índices de posición.
print("\nEjercicio 3")
for val_a, val_b in zip(a, b):
    print(val_a, val_b)

# 4. Muestra en cada iteración el valor y su índice para los elementos de b.
print("\nEjercicio 4")
b_as_strings = [str(x) for x in b]
for i, val in enumerate(b_as_strings):
    print(i, val)



# Ejercicios con listas por comprensión
print("\n-- Ejercicios con listas por comprensión --")

# 1. Crea una lista con los números del uno al 10 elevados al cuadrado
print("Ejercicio 1")
cuadrados = [num**2 for num in range(1, 11)]
print("Cuadrados: ", cuadrados)

# 2. Crea una lista con los números pares del 1 al 20
print("\nEjercicio 2")
pares = [num for num in range(1, 21) if num % 2 == 0]
print("Pares: ", pares)

# 3. Dada una lista de palabras crea una nueva lista con todas las palabras en mayúsculas
print("\nEjercicio 3")
palabras = ["sergio", "montero", "castro"]
mayusculas = [palabra.upper() for palabra in palabras]
print("Palabras en mayúsculas: ", mayusculas)

# 4. Dada una lista de números crear una nueva lista en la que se dupliquen los números impares
print("\nEjercicio 4")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impares = [num * 2 for num in numeros if num % 2 != 0]
print("Números impares: ", impares)

# 5. Dada una lista de palabras crea una lista con la segunda letra de cada palabra
print("\nEjercicio 5")
palabras = ["sergio", "montero", "castro"]
segunda_letra = [palabra[1] for palabra in palabras]
print("Segunda letra: ", segunda_letra)

# 6. Dada una lista de listas crea una lista con los elementos de todas las listas
print("\nEjercicio 6")
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
elementos = [elemento for lista in listas for elemento in lista]
print("Elementos: ", elementos)