# Ejercicios operador aritmético
print("-- Ejercicios Operador aritmético --")

# 1. Define tres variables llamadas a, b y c con los valores 50, 5.0, 100.
a = 50
b = 5.0
c = 100
print("a: ", a, ", b", b, ", c: ", c)

# 2. Define la variable d siendo la suma de a y b.
d = a + b
print("Suma: ", d)

# 3. Define la variable e siendo la resta a y b.
e = a - b
print("Resta: ", e)

# 4. Define la variable f con el resultado de la multiplicación d y e.
f = d * e
print("Multiplicación: ", f)

# 5. Define la variable g con el resultado de la división f y a.
g = f / a
print("División: ", g)

# 6. Define la variable h con el módulo de f y a.
h = f % a
print("Módulo: ", h)



# Ejercicios operadores de comparación
print("\n-- Ejercicios Operador de comparación --")

# 1. Define las variables a y b con los valores 50 y 10.
a = 50
b = 10
print("a: ", a, ", b: ", b)

# 2. Comprueba si a y b son iguales.
print("Son iguales? ", a == b)

# 3. Comprueba si a y b son diferentes.
print("Son difrerentes? ", a != b)

# 4. Comprueba si a es mayor que b.
print("a > b? ", a > b)

# 5. Comprueba si a es menor o igual que b.
print("a <= b? ", a <= b)



# Ejercicios operador de asignación
print("\n-- Ejercicios Operador de asignación --")

# 1. Define una variable y asígnale el valor 999.
x = 999
print("x: ", x)

# 2. Suma 1 a la variable anterior.
x += 1
print("x + 1: ", x)

# 3. Resta 10 a la variable anterior.
x -= 10
print("x - 10: ", x)

# 4. Multiplica por 10.
x *= 10
print("x * 10: ", x)

# 5. Divide por 5.
x /= 5
print("x / 5: ", x)

# 6. Asigna a la variable inicial el resultado del módulo de 60
x %= 60
print("x % 60: ", x)



# Ejercicios operadores lógicos
print("\n-- Ejercicios Operadores lógicos --")

# 1. Crea las variables a, b, c y d con los valores 10, 100, 200 y 300 respectivamente.
a = 10
b = 100
c = 200
d = 300
print("a: ", a, ", b: ", b, ", c: ", c, ", d: ", d)

# 2. Comprueba si a es mayor que b y c es menor que d.
print("(a > b) y (c < d)? ", (a > b) and (c < d))

# 3. Comprueba si la suma de a y b es mayor o igual que c o la suma de b y c es mayor o igual que d.
print("(a + b >= c) o (b + c >= d)? ", (a + b >= c) or (b + c >= d))



# Ejercicios operadores de pertenencia
print("\n-- Ejercicios Operadores de pertenencia --")

list1 = [1, 2, 3, 4, 5]
list2 = ['Hello', 'Word', 'Python']
list3 = ['Operator', 'Membership', 100, 200]

print("list1: ", list1)
print("list2: ", list2)
print("list3: ", list3)

# 1. Comprueba si 5 está en list1.
print("5 in list1? ", 5 in list1)

# 2. Comprueba si “Hello” y “Python” están en list2.
print("'Hello' and 'Python' in list2? ", "Hello" in list2 and "Python" in list2)

# 3. Comprueba si list2 es igual que list3.
print("list2 = list3? ", list2 == list3)



# Ejercicios con operadores bit a bit
print("\n-- Ejercicios con operadores bit a bit --")

a = 1
b = 2
print("a: ", a, ", b: ", b)

# 1. Operador AND
print("a & b: ", a & b)

# 2. Operador XOR
print("a ^ b: ", a ^ b)

# 3. Operador left shift
print("a << b: ", a << b)



# Ejercicios con operador de identidad
print("\n-- Ejercicios con operador de identidad --")

a = 3
b = 3.0

# 1. Comprueba si a es un int.
print("a es un int? ", isinstance(a, int))

# 2. Comprueba si b es un boolean.
print("b es un boolean? ", isinstance(b, bool))

# 3. Comprueba si b es un float.
print("b es un float? ", isinstance(b, float))