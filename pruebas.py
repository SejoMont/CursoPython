# Boolean
print("-- Booleanos --")

x = 42 
print("x:42 = ", bool(x))

y = 0
print("y:0 = ", bool(y))

cadena_vacia = ""
print("cad:'' = ", bool(cadena_vacia))


# Tipo númerico
print("\n-- Tipo númerico --")

print("- Sistemas numeración")
decimal = 42
binario = 0b101
octal = 0o777
hexadecimal = 0xFF

print(decimal, binario, octal, hexadecimal)

print("\n- Representacón numerica")
val = 2000000
print("2000000 = ", val)

val = 2e6
print("2e6 = ", val)

val = 2_000_000
print("2_000_000 = ", val)

print("\n- Complex")
c = 3 + 4j

print(c)

print("\n- Cadenas de caracteres")
nom = "Sejo"
ape = "Montero"
edad = 21
height = 1.7999999

# %s string, %d int, %f float
formated_str = "Hola mi nombre es %s %s, tengo %d años y mido %.2f" % (nom, ape, edad, height)
formated_str = 'Hola mi nombre es {} {}, tengo {} años y mido {:.2f}'.format(nom, ape, edad, height)
formated_str = f'Hola mi nombre es {nom} {ape}, tengo {edad} y mido {height:.2f}'

print(formated_str)

print("\n- F-String")
num = int(input("Dime un número: "))
print(f"El número {num}{'' if num % 2 == 0 else 'no'} es par")

print("\n-- Acceso a caracteres --")
name = "Sejo Montero"

first_letter = name[0]
second_letter = name[1]
thith_letter = name[2]

print(f'1 - {first_letter}, 2 - {second_letter}, 3 - {thith_letter}')

first_name = name[:4]
last_name = name[5:]
last_letter = name[-1]
inverse_name = name[::-1]

print(f'{first_name}, {last_name}, {last_letter}, {inverse_name}')

print("\n-- Metodos para cadena de caracteres --")
nom = input("Dime un nombre o número: ")

print("Len: ",len(nom))
print("Upper: ", nom.upper())
print("Lower: ", nom.lower())
print("Replace: ", nom.replace("Sejo", "Sejo Montero"))
print("Strip: ", nom.strip())
print("Split: ", nom.split())
print("Join: ", " ".join(nom))
print("Find: ", nom.find("o"))
print("Startswith: ", nom.startswith("S"))
print("Endswith: ", nom.endswith("o"))
print("IsDigit: ", nom.isdigit())
print("IsAlpha: ", nom.isalpha())
print("Isalnum: ", nom.isalnum())
print("IsSpace: ", nom.isspace())
print("Index: ", nom.index("o") if "o" in nom else "no hay 'o' en el string")

print("\n-- Tipo Lista --")
lista = [1, 2.0, "3", True, [1, 2]]

print("\n- Acceso a listas")

elemento_1 = lista[0] # Primer elemento
elemento_4 = lista[4] # Cuarto elemento
elemento_ultimo_3 = lista[-3] # Tercer elemento desde el final

print(elemento_1, elemento_4, elemento_ultimo_3)

print("\n- Unpacking y Slicing")
list1 = ['item1', 'item2', 'item3', 'item4', 'item5']


first_item, second_item, third_item, *rest = list1
print(first_item) # item1
print(second_item) # item2
print(third_item) # item3
print(rest) # ['item4', 'item5']

print("\n- Metodos para listas")
print(list1)

# append
lista.append('item6')
print("Append: ", list1)

# extend
list2 = ['item6', 'item7', 'item8', 'item9', 'item10']
list1.extend(list2)
print("Extend: ", list1)

# insert
list1.insert(0, 'item0')
print("Insert: ", list1)

# remove
list1.remove('item0')
print("Remove: ", list1)

# pop
list1.pop()
print("Pop: ", list1)

# index
print("Index: ", list1.index('item2'))

# sort
list1.sort()
print("Sort: ", list1)

# reverse
list1.reverse()
print("Reverse: ", list1) 

print("\n-- Tipo tupla --")

tupla = (1, 2.0, "3", True, [1, 2])
print(tupla)

print("\n- Metodos para tuplas")

# len
print("Len: ", len(tupla))

# max y min solo se pueden usar con tuplas que contengan solo tipos comparables
tupla_numeros = (1, 2.0, 3)
print("Max: ", max(tupla_numeros))
print("Min: ", min(tupla_numeros))

# sum
print("Sum: ", sum(tupla_numeros))

# sorted
print("Sorted: ", sorted(tupla_numeros))

# any
print("Any: ", any(tupla))

# all
print("All: ", all(tupla))


