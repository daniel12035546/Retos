from dog import Dog
from cat import Cat
from Fish import Fish
from bird import Bird
class Zoo:
    def __init__(self, name: str):
        self.name = name
        self.animals = []  

    def add_animal(self, animal):
        """Agrega un animal al zoológico."""
        self.animals.append(animal)
        print(f"{animal.name} fue agregado al zoológico {self.name}.")

    def show_animals(self):
        """Muestra todos los animales del zoológico."""
        if not self.animals:
            print(f"El zoológico {self.name} está vacío.")
        else:
            print(f"\nAnimales en el zoológico {self.name}:")
        for animal in self.animals:
            if isinstance(animal, Dog):
                print(f"Dog: {animal.name}, {animal.age} años")
            elif isinstance(animal, Cat):
                print(f"Cat: {animal.name}, {animal.age} años")
            elif isinstance(animal, Fish):
                print(f"Fish: {animal.name}, {animal.age} años, especie {animal.species}")
            elif isinstance(animal, Bird):
                print(f"Bird: {animal.name}, especie {animal.species}")
            else:
                print(f"- {animal}")
    
# Crear zoológico
zoo = Zoo("Safari Park")
# Crear animales
perro = Dog("Rex", 3)
gato = Cat("Michi", 2)

# Agregar animales al zoo
zoo.add_animal(perro)
zoo.add_animal(gato)

# Mostrar todos los animales
zoo.show_animals()

