"""
Proyecto: Creación de perros usando Programación Orientada a Objetos (POO)
Este archivo define la clase Dog y muestra cómo crear instancias, usando logging para mostrar el flujo.
"""
import logging
# Configuración básica del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Dog:
    """
    Clase Dog representa el concepto de un perro.
    En POO, una clase es un molde para crear objetos (instancias).
    """
    def __init__(self, name: str, age: int):
        """
        El método __init__ es el constructor. Se llama automáticamente al crear una instancia.
        Los atributos son las características del objeto.
        """
        self.name = name
        self.age = age
        logging.info(f"Se ha creado un perro llamado {self.name} de {self.age} años.")

    def bark(self):
        """
        Un método define el comportamiento de los objetos.
        """
        logging.info(f"{self.name} está ladrando.")
        print(f"{self.name}: ¡Guau guau!")

    def birthday(self):
        """
        Este método incrementa la edad del perro, mostrando encapsulamiento.
        """
        self.age += 1
        logging.info(f"{self.name} ahora tiene {self.age} años.")

    def fetch(self, item: str):
        """
        Método para simular que el perro trae un objeto.
        """
        logging.info(f"{self.name} está buscando {item}.")
        print(f"{self.name} ha traído {item}.")
    # Métodos para comparar edades de perros
    def edad (self, otro_perro):
        if self.age < otro_perro.age:
             print(f"{self.name} es menor que {otro_perro.name}") 
        elif self.age > otro_perro.age:
                print(f"{self.name} es mayor que {otro_perro.name}") 
        else:
            print(f"{self.name} y {otro_perro.name} tienen la misma edad") 
        
        


if __name__ == "__main__":
    # Crear instancias de la clase Dog
    dog1 = Dog("Rex",5)
    dog2 = Dog("Luna", 5)

    # Llamar métodos
    dog1.bark()
    dog2.bark()

    # Celebrar cumpleaños
    dog1.birthday()
    dog2.birthday()
 
    # Mostrar atributos
    print(f"{dog1.name} tiene {dog1.age} años.")
    print(f"{dog2.name} tiene {dog2.age} años.")
 
    # Hacer que los perros traigan objetos
    dog1.fetch("la pelota")

    dog1.edad(dog2) # Comparar edades de los perros


