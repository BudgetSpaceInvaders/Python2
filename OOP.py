class Example:
    imc = 0

    def healthCheck(self, weight, height):
        self.imc = weight / height ** 2

    def printimc(self):
        if self.imc >= 18.5 and self.imc <= 24.9:
            print("The human has a perfect weight and height with a score of", self.imc, "imc.")
        elif self.imc < 18.5:
            print("The human doesn't have enough weight having only a score of", self.imc, "imc")
        else:
            print("The human is overweight having a score of", self.imc, "imc")


bob = Example()
bob.healthCheck(60, 1.70)
bob.printimc()


class ExampleCopii(Example):
    varsta = 0

    def ageChecker(self, varsta):
        adultage = 18
        if varsta >= 18:
            print("You are an adult")
        else:
            print("You are still a child")


ion = ExampleCopii()
ion.healthCheck(10, .70)
ion.ageChecker(5)
ion.printimc()
