class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
        print(self)
    
    def __str__(self):
        m = "this is a:{ty}, color:{co}, flavor:{fl}".format(ty=type(self), co=self.color, fl=self.flavor)
        return m

class Apple(Fruit):
    pass

apple1 = Apple('green', 'tart')

#print(type(Apple))
print(type(apple1))




class Animal:
    sound = ''
    def __init__(self, name):
        self.name = name
        print(self)
        self.speak()

    def speak(self):
        print("{so}! I'm {na}! {so}!".format(na=self.name, so=self.sound*2))

    def __str__(self):
        m = "this is a:{ty}".format(ty=type(self))
        return m
    
class Piglet(Animal):
    sound = 'Oink!'

class Dog(Animal):
    sound = 'Guag!'

hamlet = Piglet('Hampet')
shasha = Dog('Shasha')
# hamlet.name = 
# hamlet.speak()


class Clothing:
    
    material = ""
    
    def __init__(self,name):
        self.name = name
    
    def checkmaterial(self):
        print("This {} is made of {}".format(self.name, self.material))
			
class Shirt(Clothing):
    material = "Cotton"

polo = Shirt("Polo")
polo.checkmaterial()
