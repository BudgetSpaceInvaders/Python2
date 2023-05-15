import math


class Figura:
    def aria(self):
        pass


class Cerc(Figura):
    def __init__(self, raza):
        self.raza = raza

    def aria(self):
        return math.pi * self.raza ** 2


figura1 = Cerc(5)
print(figura1.aria())


class Dreptunghi(Figura):
    def __init__(self, lung, lat):
        self.lung = lung
        self.lat = lat

    def aria(self):
        return self.lat * self.lung


figura2 = Dreptunghi(8, 4)
print(figura2.aria())
