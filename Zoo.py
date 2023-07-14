class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Lion(Animal):
    def __init__(self, name, age, sex):
        super().__init__(name, age)
        self.sex = sex

    def make_sound(self):
        return "grraaaauuuu"


class Elephant(Animal):
    def __init__(self, name, age, lentrunk):
        super().__init__(name, age)
        self.lentrunk = lentrunk

    def make_sound(self):
        return "bahruuuuuuhhhhaaaaa"


class Penguin(Animal):
    def __init__(self, name, age, fly):
        super().__init__(name, age)
        self.fly = fly

    def make_sound(self):
        return "HONK!!!"


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def show_animals(self):
        for animal in self.animals:
            print(f"Name: {animal.get_name()}, Age: {animal.get_age()}, Sound: {animal.make_sound()}")


lion1 = Lion("Simba", 10, "male")
lion1.make_sound()
lion1.get_age()
lion1.get_name()

elephant1 = Elephant("Dumbo", 15, "2 meters")
elephant1.make_sound()
elephant1.get_age()
elephant1.get_name()

penguin1 = Penguin("Pingu", 13, False)
penguin1.make_sound()
penguin1.get_age()
penguin1.get_name()
