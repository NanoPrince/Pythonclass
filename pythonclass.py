# define  the vehicle class
from io import BufferedRandom


class vehicle:
    # brand = "toyota, honda"
    # model = 0
    # color = "red, blue"
    # price = 0

    # def cardescription(self):
    #     desc_str = "%s is a %s %s worth $%.2f." % (self.brand, self.model, self.color, self.price)
    #     return desc_str
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (
            self.name, self.color, self.kind, self.value)
        return desc_str


# creation of the objects
car1 = vehicle()
car2 = vehicle()

car1.color = "red convertible"
car1.price = 60000
car1.name = "Fer"

car2.color = "blue van"
car2.price = 10000
car2.name = "Jump"

# test code by printing car types
print(car1.description())
print(car2.description())
