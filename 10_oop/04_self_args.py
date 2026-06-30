class Chaicup:

    size = 150  # ml

    # self is the parameter that all you are defining the namespace of the class

    def describe(self):
        return f"A {self.size}ml chai cup"


cup = Chaicup()
print(cup.describe())
print(Chaicup.describe(cup))

cup_two = Chaicup()
cup_two.size = 200
print(Chaicup.describe(cup_two))
