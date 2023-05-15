class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def mancare(self):
        print("Animalul mananca")

    def sunet(self):
        print("Animalul face sunete")


class Dog(Animal):
    def sunet(self):
        print("Cainele latra")


class Cat(Animal):
    def sunet(self):
        print("Pisica toarce si miauna")


animal1 = Animal("cow", 3)
animal1.sunet()
animal1.mancare()
dog1 = Dog("Rex", 13)
dog1.sunet()
dog1.mancare()
cat1 = Cat("Tom", 13)
cat1.sunet()
cat1.mancare()
