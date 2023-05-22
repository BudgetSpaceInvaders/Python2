class Computer:
    def __init__(self, name, memory):
        self.name = name
        self.memory = memory
        self.__price = 1200

    def selling_price(self):
        print("The selling price of a", self.name, "with", self.memory, "GB is", self.__price, "euro")

    def change_price(self, price):
        self.__price = price


comp1 = Computer("Linux", "1024")
comp1.selling_price()
comp1.change_price("900")
