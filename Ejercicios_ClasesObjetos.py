# Ejercicio FirstExercise
print("-- Ejercicio FirstExercise --")

# 1.1. Define una clase vacía llamada FirstExercise.
# 1.2. Modifica la clase anterior. La clase debe recibir obligatoriamente las variables number y chapter.
class FirstExercise:
    def __init__(self, number, chapter):
        self.number = number
        self.chapter = chapter
    
    def print_number(self):
        print(f"Numero: {self.number}")

# 1.3. Instancia un objeto con los valores 6 y “Clases y objetos”.
obj = FirstExercise(6, "Clases y objetos")

# 1.4. Añade un método que imprima por pantalla el número.
obj.print_number()

# 1.5. Crea una clase Circle que dado un radio permita consultar el área, el perímetro y permita modificar el radio.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius

circulo = Circle(15)
print(f"Radio = {circulo.radius}, Área = {circulo.area()}, Perímetro = {circulo.perimeter()}")

nuevoRadio = float(input("Introduce nuevo radio: "))
circulo.set_radius(nuevoRadio)
print(f"Radio = {circulo.radius}, Área = {circulo.area()}, Perímetro = {circulo.perimeter()}")

# 2.1. Cree una clase Vehicle que reciba el nombre, velocidad máxima y el kilometraje.
class Vehicle:
    owner = "Nter" # 2.5. Defina la variable owner que tenga el valor “Nter” para todos los objetos de la clase.
    
    def __init__(self, name, max_speed, km):
        self.name = name
        self.max_speed = max_speed
        self.km = km
    
    # 2.3. Método para imprimir la capacidad de cualquier vehículo
    def print_capacidad(self, capacity):
        print(f"La capacidad de {self.name} es de {capacity}")

# 2.2. Cree una clase Bus que herede todos los métodos y variables de Vehicle.
class Bus(Vehicle):
    def __init__(self, name, max_speed, km):
        super().__init__(name, max_speed, km)  # Llama al constructor de Vehicle

    # 2.4. Método para imprimir la capacidad, con un valor por defecto de 50
    def print_capacidad(self):
        print(f"La capacidad de {self.name} es de 50")

vehicle1 = Vehicle("Coche", 180, 15000)
vehicle1.print_capacidad(5)  

bus1 = Bus("Autobús", 100, 50000)
bus1.print_capacidad()  

print(f"El propietario de {vehicle1.name} es {vehicle1.owner}")
print(f"El propietario de {bus1.name} es {bus1.owner}")


