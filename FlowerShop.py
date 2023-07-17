class Flower:
    def __init__(self, color):
        self.color = color
        self.name = "Place holder"
        self.special_thing = "place holder"

    def get_color(self):
        return self.color

    def get_name(self):
        return self.name

    def bloom(self):
        print("The", self.get_name(), "has bloomed.")

    def get_special_thing(self):
        return self.special_thing


class Rose(Flower):
    def __init__(self, color, fragrance):
        super().__init__(color)
        self.name = "Rose"
        self.fragrance = fragrance
        self.special_thing = self.fragrance


class Sunflower(Flower):
    def __init__(self, color, stem_height):
        super().__init__(color)
        self.name = "Sunflower"
        self.stem_height = stem_height
        self.special_thing = self.stem_height


class Orchid(Flower):
    def __init__(self, color, nr_petals):
        super().__init__(color)
        self.name = "Orchid"
        self.nr_petals = nr_petals
        self.special_thing = self.nr_petals


class FlowerShop:
    def __init__(self):
        self.flowers = []

    def adder(self, flower):
        self.flowers.append(flower)

    def remover(self, flower):
        self.flowers.remove(flower)

    def shower(self):
        print("======================================")
        for x in self.flowers:
            print(f"Flower: {x.get_name()}, color: {x.get_color()}. {x.get_special_thing()}")
        print("======================================")


flowerShop = FlowerShop()
rose1 = Rose("Red", "Tea aroma!")
rose1.get_name()
rose1.get_color()
rose1.bloom()
rose1.get_special_thing()
flowerShop.adder(rose1)
sunflower1 = Sunflower("Yellow and black", "The stems height is 2 meters!")
sunflower1.get_name()
sunflower1.get_color()
sunflower1.bloom()
flowerShop.adder(sunflower1)
orchid1 = Orchid("Red", "Has 3 petals!")
orchid1.get_name()
orchid1.get_color()
orchid1.bloom()
flowerShop.adder(orchid1)
flowerShop.shower()
# flowerShop.remover(orchid1)
# flowerShop.shower()
