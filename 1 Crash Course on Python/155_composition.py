class Repository:
    """A repository class that contains packages"""
    def __init__(self):
        self.packages = {}
    
    def add_package(self, package):
        self.packages[package.name] = package

    def total_size(self):
        result = 0
        for p in self.packages.values():
            result += p.size
        return result


# Let’s expand a bit on our Clothing classes 
# from the previous in-video question. 
# Your mission: Finish the "Stock_by_Material" method 
# and iterate over the amount of each item of a given material 
# that is in stock. When you’re finished, 
# the script should add up to 10 cotton Polo shirts.

class Clothing:
    stock = { 'name': [], 'material' :[], 'amount':[]}
    
    def __init__(self, name):
        material = ""
        self.name = name
    
    def add_item(self, name, material, amount):
        Clothing.stock['name'].append(self.name)
        Clothing.stock['material'].append(self.material)
        Clothing.stock['amount'].append(amount)
    
    def add_items(self, amount):
        Clothing.stock['name'].append(self.name)
        Clothing.stock['material'].append(self.material)
        Clothing.stock['amount'].append(amount)

    def Stock_by_Material(self, material):
        count = 0
        n = 0
        for item in Clothing.stock['material']:
            if item == material:
                count += Clothing.stock['amount'][n]
            n+=1
        return count
    
    def Stock_by_Material_2(self, material):
        count = 0
        for i, item in enumerate(Clothing.stock['material']):
            if item == material:
                count += Clothing.stock['amount'][i]
        return count

class shirt(Clothing):
    material="Cotton"

class pants(Clothing):
    material="Cotton"
  
polo = shirt("Polo")
pique = shirt("Pique")
sweatpants = pants("Sweatpants")
print(Clothing.stock)
polo.add_item(polo.name, polo.material, 4)

print(Clothing.stock)
pique.add_items(5)

print(Clothing.stock)
pique.add_item(sweatpants.name, sweatpants.material, 6)
print(Clothing.stock)

print(polo.Stock_by_Material("Cotton"))
print(polo.Stock_by_Material_2("Cotton"))

