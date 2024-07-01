## A Class is like an object constructor, or a "blueprint" for creating objects.

# Car class
class Car:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    def move(self):
        print(f"{self.name} is moving...")
        
    
# ElectricCar class        
class ElectricCar(Car):
    def __init__(self, name, brand, battery):
        super().__init__(name, brand)
        self.battery = battery

    def move(self):
        print(f"{self.name} is moving silently...")
        
    def charge(self):
        print(f"{self.name} is charging...")
        
 
# Plane class       
class Plane():
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    def move(self):
        print(f"{self.name} is flying...")
        

# Boat class
class Boat():
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    def move(self):
        print(f"{self.name} is sailing...")
        
        
# Race classes
benz = Car("Benz", "Mercedes")
# tesla = ElectricCar("Tesla", "Tesla", "1000")
boeing = Plane("Boeing", "Boeing")
soyuz = Boat("Soyuz", "Soyuz")

for x in [benz, boeing, soyuz]:
    x.move()