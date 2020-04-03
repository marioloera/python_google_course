# str is used when printing objects
class Apple:

    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "This apple is {cl} and its flavor is {fl}".format(cl = self.color, fl = self.flavor)


jonagold = Apple('red', 'sweet')
print(jonagold.color)
print(jonagold.flavor)
print(jonagold)

class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is {n}".format(n=self.name) 

# Create a new instance with a name of your choice
some_person = Person('Joe')  
# Call the greeting method
print(some_person.greeting())

print(type(some_person))
