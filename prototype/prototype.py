import copy

class Animal:
    # Construtor
    def __init__(self, species, name, sound):
        self.species = species
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} the {self.species} says {self.sound}")

    def clone(self):
        return copy.deepcopy(self)



if __name__ == "__main__":
    # Criação de um protótipo
    dog_prototype = Animal("Dog", "Krypto", "Woof")
    cat_prototype = Animal("Cat", "Bongo", "Meow")

    # Clonando o protótipo
    another_dog = dog_prototype.clone()
    another_cat = cat_prototype.clone()

    # Modificando as cópias
    another_dog.name = "Max"
    another_cat.name = "Felix"

    # Usando os objetos clonados
    dog_prototype.make_sound()   # Output: Krypto the Dog says Woof
    another_dog.make_sound()     # Output: Max the Dog says Woof
    cat_prototype.make_sound()   # Output: Bongo the Cat says Meow
    another_cat.make_sound()     # Output: Felix the Cat says Meow
