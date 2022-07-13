class Animal:
    sound = ""
    name = ""
    habitat = ""
    feedingMethod = ""

    def info(self):
        message = "%s is a %s animal. It's feeding method is %s. It %ss" % (self.name, self.habitat, self.feedingMethod, self.sound)
        return message


type1 = Animal()

type1.sound = "bark"
type1.name = "dog"
type1.habitat = "land"
type1.feedingMethod = "herbiverous"


type2 = Animal()

type2.sound = "whine"
type2.name = "horse"
type2.habitat = "land"
type2.feedingMethod = "herbiverous"


print(type1.info())
print()
print(type2.info())