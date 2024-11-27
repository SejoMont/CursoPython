from datetime import datetime, time

# Ejercicios númericos
print("\n-- Ejercicios númericos --")

# 1. Define un número de tipo int.
numInt = 1
print("Número Int: ", numInt)

# 2. Define un número de tipo float.
numFloat = 1.0
print("Número Float: ", numFloat)

# 3. Define un número de tipo complex.
numComplex = 1j
print("Número Complex: ", numComplex)

# 4. Muestra por pantalla la parte real del número definido en el punto 3.
print("Parte real: ",numComplex.real)

# 5. Muestra por pantalla la parte imaginaria del número definido en el punto 3
print("Parte imaginaria: ",numComplex.imag)



# Ejercicios boolean
print("\n-- Ejercicios boolean --")

# 1. Define una variable con valor True.
boolTrue = True
print("Boolean True: ", boolTrue)

# 2. Define una variable con valor False.
boolFalse = False
print("Boolean False: ", boolFalse)

# 3. Define una variable con valor True mediante un entero
boolNone = 1
print("Boolean True Int: ", boolNone)



# Ejercicios string
print("\n-- Ejercicios string --")

# 1. Define una variable con un string con el valor “ Master Python”.
string1 = " Master Python"
print("String: ", string1)

# 2. Muestra la longitud de la variable anterior.
print("Longitud: ", len(string1))

# 3. Muestra el primer carácter del string.
print("Primer carácter: ", string1[0])

# 4. Muestra el penúltimo carácter del string.
print("Penúltimo carácter: ", string1[-2])

# 5. Elimina los espacios iniciales del string.
print("Sin espacios iniciales: ", string1.lstrip())

# 6. Muestra los caracteres en posiciones impares.
print("Caracteres en posiciones impares: ", string1[1::2])

# 7. Convierte todo el string en minúscula.
print("Todo en minuscula: ", string1.lower())

# 8. Separa el string por espacios en blanco.
print("Separado por espacios: ", string1.split(" "))

# 9. Reemplaza “python” por “JAVA”.
print("Reemplazado: ", string1.replace("Python", "JAVA"))



# Ejercicios con listas
print("\n-- Ejercicios con listas --")

lista = [10, 20, 'Hello', 20.5]
print("Lista: ", lista)

# 1. Añade “Word” al final de la lista.
lista.append("Word")
print("Añadido al final: ", lista)

# 2. Añade “Python” al principio de la lista.
lista.insert(0, "Python")
print("Añadido al principio: ", lista)

# 3. Elimina el segundo valor de la lista.
del lista[1]
print("Eliminado: ", lista)

# 4. Crea una segunda lista con los valores 20, 40, ‘Bye’ (utiliza una forma diferente que en el inicio)
lista2 = list((20, 40, "Bye"))
print("Segunda lista: ", lista2)

# 5. Une las dos listas.
lista.extend(lista2)

# 6. Muestra la lista final.
print("Final: ", lista)



# Ejercicios con set
print("\n-- Ejercicios con set --")

# 1. Define un conjunto con los valores coche, motocicleta, bicicleta.
set1 = {"coche", "motocicleta", "bicicleta"}
print("Set: ", set1)

# 2. Añade avión al conjunto.
set1.add("avión")
print("Añadido: ", set1)

# 3. Elimina coche del conjunto.
set1.remove("coche")
print("Eliminado: ", set1)

# 4. Crea otro conjunto con los valores avión, coche, tractor (utiliza una forma diferente que en el punto 1).
set2 = {"avión", "coche", "tractor"}
print("Segundo set: ", set2)

# 5. Crea otro conjunto con los valores que se repitan en los conjuntos anteriores.
set3 = set1 & set2
print("Intersección: ", set3)

# 6. Muestra un conjunto con todos los valores que pertenecen al conjunto creado en el punto 1 y punto 4
set4 = set1 | set2
print("Union: ", set4)



# Ejercicios con diccionarios
print("\n-- Ejercicios con diccionarios --")

# 1. Define el diccionario usando dict().
dict1 = dict(coche=10, motocicleta=20, camion=30)
print("Diccionario: ", dict1)

# 2. Define el diccionario usando { }.
dict2 = {"coche":10, "motocicleta":20, "camion":30}
print("Diccionario: ", dict2)

# 3. Muestra los valores del diccionario.
print("Valores: ", dict1.values())

# 4. Muestra las claves del diccionario.
print("Claves: ", dict1.keys())

# 5. Muestra el valor de coche.
print("Coche: ", dict1["coche"])

# 6. Añade al diccionario avion con valor 100.
dict1["avion"] = 100

# 7. Muestra los elementos del diccionario.
print("Elementos: ", dict1.items())



# Ejercicios con tuplas
print("\n-- Ejercicios con tuplas --")

tupla = ("coche", "motocicleta", "camion")
print("Tupla: ", tupla)

# 1. Accede al primer y último elemento de la tupla e imprime sus valores
print("Primer elemento: ", tupla[0])
print("Ultimo elemento: ", tupla[-1])

# 2. Crea otra tupla de forma distinta a la del inicio con los valores: perro, gato y naranja.
tupla2 = tuple(["perro", "gato", "naranja"])
print("Tupla 2: ", tupla2)

# 3. Concatena las dos tuplas en una nueva con el nombre ‘tupla_concatenada’
tupla_concatenada = tupla + tupla2
print("Tupla concatenada: ", tupla_concatenada)

# 4. Cuenta el número de elementos de la tupla del punto 3
print("Numero de elementos: ", len(tupla_concatenada))

# 5. Encuentra el índice del elemento perro dentro de ‘tupla_concatenada’
print("Indice de perro: ", tupla_concatenada.index("perro"))

# 6. Desempaqueta ‘tupla_concatenada’ en las variables (por este orden) tp1, tp2, tp3 y el resto en tp4
tp1, tp2, tp3, *tp4 = tupla_concatenada

# 7. Imprime los valores de las variables (tp1 = coche, tp2 = motocicleta, tp3 = camion...)
print("tp1: ", tp1)
print("tp2: ", tp2)
print("tp3: ", tp3)
print("tp4: ", tp4)

# 8. Añade un nuevo elemento a 'tupla_concatenada'
tupla_concatenada = tupla_concatenada + ("barco",)

# 9. Muestra los elementos de 'tupla_concatenada'
print("Tupla concatenada: ", tupla_concatenada)



# Ejercicios con fechas
print("\n-- Ejercicios con fechas --")

fechas = ['2024-09-09', '2023-08-15', '2022-07-01']
horas = ['14:30:00', '09:15:00', '23:59:59']

print("Fechas: ", fechas)
print("Horas: ", horas)

# 1. Convierte cada cadena de la lista fechas a un objeto date.
fechas_date = [datetime.strptime(fecha, "%Y-%m-%d").date() for fecha in fechas]
print("Fechas date: ", fechas_date)

# 2. Convierte cada cadena de la lista horas a un objeto time
horas_time = [datetime.strptime(hora, "%H:%M:%S").time() for hora in horas]
print("Horas time: ", horas_time)

# 3. Combina cada elemento de los objetos date y los objetos time de los dos ejercicios anteriores para crear una
#    lista de objetos datetime.
fechas_horas = [datetime.combine(fecha, hora) for fecha, hora in zip(fechas_date, horas_time)]
print("Fechas y horas: ", fechas_horas)

# 4. Calcula los días de diferencia que hay entre los objetos date resultantes del ejercicio 1 y la fecha actual.
fechas_diferencia = [(fecha - datetime.now().date()).days for fecha in fechas_date]
print("Diferencia de fechas en días: ", fechas_diferencia)

# 5. Elige una fecha de los objetos date resultantes del ejercicio 1 y cambiar su año a 2025.
fechas_2025 = [fecha.replace(year=2025) for fecha in fechas_date]
print("Fechas 2025: ", fechas_2025)

# 6. Convierte cada objeto datetime resultante del ejercicio 3 en una cadena con el formato DD/MM/YYYY HH:MM
fechas_cadena = [fecha.strftime("%d/%m/%Y %H:%M") for fecha in fechas_horas]
print("Fechas cadena: ", fechas_cadena)
