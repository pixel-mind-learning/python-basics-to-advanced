class Chai:
    def_init_(self, sweetness, milk_level):
        self.sweetness = sweetness
        self.milk_level = milk_level
    
    def sip(self):
        print("Sipping chai")

    def add_sugar(self, amount):
        print("added the sugar")

my_chai = Chai(sweetnedd=3, milk_level=2)

my_chai.add_sugar(3)