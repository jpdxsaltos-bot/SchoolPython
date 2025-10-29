class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Some animal sound")

    def print_information(self):
        print(f"Name: {self.name}, Species: {self.species}")

class Lion(Animal):

    def __init__(self, name):
        super().__init__(name, "Lion")

    def make_sound(self):
        print("Roar!")

class Elephant(Animal):

    def __init__(self, name):
        super().__init__(name, "Elephant")

    def make_sound(self):
        print("Trumpet!")

class Snake(Animal):

    def __init__(self, name):
        super().__init__(name, "Snake")

    def make_sound(self):
        print("Hiss!")

class Zoo:

    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} the {animal.species} was added to the zoo.")

    def show_all_animals(self):
        print("\nAnimals in the zoo:")
        for animal in self.animals:
            animal.print_information()
        print(f"Total animals: {len(self.animals)}")

    def make_all_sounds(self):
        print("\nAnimal sounds:")
        for animal in self.animals:
            animal.make_sound()

zoo = Zoo()

zoo.add_animal(Lion("Simba"))
zoo.add_animal(Elephant("Dumbo"))
zoo.add_animal(Snake("Nagini"))

zoo.show_all_animals()
zoo.make_all_sounds()