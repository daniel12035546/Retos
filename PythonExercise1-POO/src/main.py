from dog import Dog
from cat import Cat
from Fish import Fish
from zoo import Zoo

# Crear zoológico
zoo = Zoo("Safari Park")

# Crear animalesgtv
perro = Dog("Rex", 3)
gato = Cat("Michi", 2)
pez = Fish("Nemo", 1, "Payaso")

# Agregar animales al zoo
zoo.add_animal(perro)
zoo.add_animal(gato)
zoo.add_animal(pez)

# Mostrar todos los animales
zoo.show_animals()
