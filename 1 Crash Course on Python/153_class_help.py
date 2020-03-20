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

#print(help(Apple)) # very limited

# docstring  A docstring is a brief text that explains what something does
# when type help(class) or help(funciton) the docsting will appear

def to_seconds(hours, minutes, seconds):
    """Returns the seconts in the given hours, minutes and seconds."""
    return hours*60**2 + minutes*60 + seconds

print(to_seconds(1, 0, 1))
print(to_seconds(1, 1, 0))
print(to_seconds(1, 0, 0))
help(to_seconds)

class Person:
    """Class that represents a person wiht a name"""
    
    def __init__(self, name):
        """Create an instance with a name"""
        self.name = name
    
    def greeting(self):
        """Outputs a message with the name of the person"""
        print("Hello! My name is {name}.".format(name=self.name)) 

help(Person)
