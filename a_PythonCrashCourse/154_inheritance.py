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
    kind = '0'
    def __init__(self, name, _kind='1'):
        print('\nAnimal Class __init__')
        self.name = name
        self.kind = _kind
        print(self)
        self.speak()

    def speak(self):
        print("{sound}! I'm {name}! {sound}!".format(
                            name=self.name,
                            sound=self.sound*2))
        print(self.kind)

    def __str__(self):
        m = "this is a:{ty}".format(ty=type(self))
        return m
    
class Piglet(Animal):
    sound = 'Oink!'
    print('\nPiglet Class: ' + Animal.kind) 



class Dog(Animal):
    sound = 'Guag!'
    print('\nDog Class: ' + Animal.kind) 

print('initialization:\n')
hamlet = Piglet('Hampet', '2')
shasha = Dog('Shasha', '3')
# hamlet.name = 
# hamlet.speak()
exit()

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
