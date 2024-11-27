# Ejercicios con funciones
print("\n-- Ejercicios con funciones --")

# 1. Define una función llamada showAnimal que reciba dos argumentos name y n_legs e imprima esta
#    información por pantalla.
print("\nEjercicio 1")

def showAnimal(name, n_legs):
    print("Animal: ", name, " con ", n_legs, " patas")

showAnimal("perro", 4)

# 2. Define una función que puede recibir cualquier número de argumentos e imprima cuántos argumentos
#    ha recibido.
print("\nEjercicio 2")

def showArgs(*args):
    print("Argumentos: ", len(args))

showArgs(1,2,3,4,5)

# 3. Define una función que recibiendo dos números, devuelva la suma y la resta de ellos en una sola
#    llamada.
print("\nEjercicio 3")

def sumaResta(num1, num2):
    return num1 + num2, num1 - num2

print(sumaResta(10, 20))

# 4. Define una función que recibiendo dos números devuelva la multiplicación.
print("\nEjercicio 4")

def multiplicacion(num1, num2):
    return num1 * num2

print(multiplicacion(10, 20))

# 5. Define una función que recibiendo dos números devuelva el módulo.
print("\nEjercicio 5")

def modulo(num1, num2):
    return num1 % num2

print(modulo(10, 20))

# 6. Define una función que recibiendo una función del ejercicio 4 o ejercicio 5 y dos valores numéricos
#    devuelva su resultado.
print("\nEjercicio 6")

def operacion(funcion, num1, num2):
    return funcion(num1, num2)

print(operacion(multiplicacion, 10, 20))
print(operacion(modulo, 10, 20))

# 7. Define una función que reciba el nombre y email de una persona. Si no recibe email, se asignará “Sin
#    determinar”. La función debe imprimir el nombre y email de la persona.
print("\nEjercicio 7")

def showPerson(name, email="Sin determinar"):
    print("Persona: ", name, ", email: ", email)

showPerson("Sejo")
showPerson("Sejo", "sejo@gmail.com")

# 8. Define una función que recibiendo un entero positivo, irá sumando este número a su anterior hasta
#    llegar a 0 y devolverá el resultado final.
print("\nEjercicio 8")

def sumar(num):
    if num > 0:
        return num + sumar(num - 1)
    return 0

print(sumar(10))



# Ejercicios con funciones
print("\n-- Ejercicios con funciones anónimas --")

# 1. Define una función lambda que calcule el cuadrado de un número
print("\nEjercicio 1")

cuadrado = lambda x: x**2
print("10: ",cuadrado(10))

# 2. Define una función lambda que devuelva True si el cuadrado de un número es mayor que 999 si no
#    devuelve False.
print("\nEjercicio 2")

esCuadrado999 = lambda x: True if x**2 > 999 else False
print("10: ",esCuadrado999(10))
print("1000: ", esCuadrado999(1000))

# 3. Define una función lambda que reciba dos números y devuelva el resultado de su multiplicación.
print("\nEjercicio 3")

multiplicar = lambda x, y: x * y
print("3 * 27 = ",multiplicar(3, 27))

# 4. Utilizando la función sorted() y lambda ordena una lista de palabras teniendo en cuenta la segunda letra
#    de cada palabra.
print("\nEjercicio 4")

palabras = ["sergio", "montero", "castro"]

print(sorted(palabras, key=lambda x: x[1]))



# Ejercicios con funciones de orden superior
print("\n-- Ejercicios con funciones de orden superior --")

# 1. Define una función que devuelva una lista con el doble de todos los elementos de la lista inicial.
print("\nEjercicio 1")

def listaDobles(lista):  
    return list(map(lambda x: x * 2, lista))

print(listaDobles([1,2,3,4,5]))

# 2. Define una función que eleve al cuadrado los elementos que sean pares.
print("\nEjercicio 2")

def cuadradosPares(lista):
    return list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, lista)))

print(cuadradosPares([1,2,3,4,5]))

# 3. Define una función que dada dos listas sume los elementos de la misma posición.
print("\nEjercicio 3")

def sumarListas(lista1, lista2):
    return list(map(lambda x, y: x + y, lista1, lista2))

print(sumarListas([1,2,3,4,5], [6,7,8,9,10]))

# 4. Define una función que dado una lista de strings devuelva una lista con el número de ‘a’ que aparece en
#    cada string.
print("\nEjercicio 4")

def countA(lista):
    return list(map(lambda x: x.count("a"), (lista)))

print(countA(["Sejo", "Natalia", "Alicia"]))

# 5. Define una función que dado una lista sólo devuelva los elementos que son negativos.
print("\nEjercicio 5")

def negativos(lista):
    return list(filter(lambda x: x < 0, (lista)))

print(negativos([-3,5,7,-1]))

# 6. Define una función que dado un string devuelva la lista de vocales que aparecen.
print("\nEjercicio 6")

def vocales(string):
    return list(filter(lambda x: x in "aeiou", (string)))

print(vocales("Sejo"))

# 7. Define una función que dado una lista devuelva la multiplicación de todos los elementos.
from functools import reduce

print("\nEjercicio 7")

def listaMult(lista):
    result = 1
    for num in lista:
        result *= num
    return result

print(listaMult([1,2,3,4,5]))

#8. Dado un string extraer los números que aparecen en el texto y devolver su suma.
print("\nEjercicio 8")

def sumarNumeros(string):
    result = 0
    for num in string:
        if num.isdigit():
            result += int(num)
    return result

print(sumarNumeros("1234"))