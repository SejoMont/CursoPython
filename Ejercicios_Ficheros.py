# Ejercicios Ficheros
print("\n-- Ejercicios Ficheros --")

line1 = "Es mi primera línea."
line2 = "Es mi segunda línea."
line3 = "Es mi tercera línea."
line4 = "¡Es el final del fichero!"

# 1. Crea un fichero vacío llamado primerfichero.txt sin usar with.
archivo = open("primerfichero.txt", "w")
print("primerfichero.txt creado")

# 2. Crea un segundo fichero vacío llamado segundofichero.txt usando with.
with open("segundofichero.txt", "w") as archivo2:
    pass
print("segundofichero.txt creado")

# 3. Escribe line1 en primerfichero.txt
archivo.write(line1)
print("line1 escrita en primerfichero.txt")

# 4. Escribe line2, line3 y line4 en segundofichero.txt cada uno en una línea.
with open("segundofichero.txt", "w") as archivo2:
    archivo2.write(line2 + "\n")
    archivo2.write(line3 + "\n")
    archivo2.write(line4)
print("line2, line3 y line4 escritas en segundofichero.txt")

# 5. Lee primerfichero.txt y añade su contenido al final de segundofichero.txt.
with open("segundofichero.txt", "a") as archivo2:
    with open("primerfichero.txt") as archivo:
        for linea in archivo:
            archivo2.write(linea)
print("primerfichero.txt leido y anadido al final de segundofichero.txt")