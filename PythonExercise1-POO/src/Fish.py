
def atributos_objeto():  # aquí definimos los atributos de nuestro pez
    name = "nemo"
    age = 12
    species = "payaso"
    return name, age, species

class Fish:  # aquí creamos la clase llamada pez
    def __init__(self, name="fish", age=5, species="goldfish"):
        self.name = name
        self.age = age
        self.species = species

    def swim(self):  # aquí definimos el método "swim"
        return f"Nombre: {self.name}, Edad: {self.age}, Especie: {self.species}"

# aquí llamamos a la función para imprimir los atributos del pez

name, age, species = atributos_objeto()
pez = Fish(name, age, species)
print(pez.swim())

