from zoo import zoo  # importamos la clase zoo desde el archivo zoo.py
class veterinarian:
    # ...código existente...    
    def __init__(self):
     self.name  =  "Dr. Simi"
    

    def  checkup(self, zoo ):
        if not zoo.animals:
            print(f"El zoológico {zoo.name} no tiene animales para revisar.")
            return

        print(f"\n {self.name} comienza la revisión en {zoo.name}:\n")

        for animal in zoo.animals:
            print(f" Revisando a {animal.name}...")
            if hasattr(animal, "age"):
                print(f"   {animal.name} tiene {animal.age} años.")
            if hasattr(animal, "species"):
                print(f"   Es de la especie {animal.species}.")
            print("  Revisión completada.\n")

if __name__ == "__main__":
    vet = veterinarian()
    vet.checkup(zoo)