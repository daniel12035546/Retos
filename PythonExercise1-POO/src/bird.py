"""
Proyecto: Ejemplo de herencia en POO con aves.
Este archivo define la clase Bird y la clase Eagle que hereda de Bird.
Incluye logging y comentarios explicativos sobre herencia.
"""
import logging
# Configuración básica del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Bird:
    """
    Clase base Bird representa el concepto general de un ave.
    En POO, una clase base puede ser heredada por otras clases más específicas.
    """
    def __init__(self, name: str, age: int, species: str):
        self.name = name
        self.age = age
        self.species = species
        logging.info(f"Se ha creado un ave de especie {self.species} llamada {self.name} de {self.age} años.")

    def sing(self):
        """
        Método que representa el canto del ave.
        """
        logging.info(f"{self.name} está cantando.")
        print(f"{self.name}: ¡Pío pío!")


    def birthday(self):
        self.age += 1
        logging.info(f"{self.name} ahora tiene {self.age} años.")

    def migrate(self):
        logging.info(f"{self.name} esta migrando.")
        print(f"{self.name} esta migrando a un lugar lejano.")

# Ejemplo de herencia: Eagle hereda de Bird
class Eagle(Bird):
    """
    Clase Eagle hereda de Bird.
    En POO, la herencia permite que una clase hija obtenga atributos y métodos de la clase padre.
    """
    def __init__(self, name: str, age: int):
        # Llama al constructor de Bird con especie fija "Águila"
        super().__init__(name, age, "Águila")
        logging.info(f"Se ha creado un águila llamada {self.name}.")

    def fly(self):
        """
        Método propio de Eagle, además de los heredados de Bird.
        """
        logging.info(f"{self.name} está volando alto.")
        print(f"{self.name}: ¡Estoy volando alto!")
        
    def altitude(self, meters: int):
        logging.info(f"{self.name} ha alcanzado una altitud de {meters} metros.")
        print(f"{self.name} ha alcanzado una altitud de {meters} metros.")

class Parrot(Bird):
    """
    Clase Parrot hereda de Bird.
    """
    def talk(self):
        logging.info(f"{self.name}, Andres caicedo una vez dijo")
        print(f"{self.name}: Tu, no te detengas ante ningún reto. Y no pases a formar parte de ningún gremio. Que nunca te puedan definir ni encasillar. Que nadie sepa tu nombre y que nadie amparo te dé.")

if __name__ == "__main__":
    Eagle1 = Eagle("Pablo", 6)
    Eagle1.birthday()
    Eagle1.fly()  
    Eagle1.altitude(1000) 
    loro = Parrot("Lorenzo", 3, "Loro")
    Eagle1.migrate()
