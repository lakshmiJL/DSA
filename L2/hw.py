class Car:
    def __init__(self, brand, model, fuel, color):
        self.brand = brand
        self.model = model
        self.fuel = fuel
        self.color = color
    
    def getColor(self):
        return self.color
     
    def setColor(self, newColor):
        self.color = newColor
        
    def showCar(self):
        print("Car - {} - {}, Fuel Type - {}, Color - {}".format(self.brand, self.model, self.fuel, self.color))
        
    
class SUV(Car):
    def __init__(self, brand, model, fuel, color, transmission, turbo):
        Car.__init__(self, brand, model, fuel, color)
        self.transmission = transmission
        self.turbo = turbo
        
    def showCar(self):
        print("Car - {} - {}, Fuel Type - {}, Color - {}, Transmission - {}, Turbo True/False - {}".format(self.brand, self.model, self.fuel, self.color, self.transmission, self.turbo))
        






# Concept of Inheritance

audiQ3 = SUV("Audi", "Q3", "Disel", "White", "Automatic", True)

# Inherited from class Car
print(audiQ3.getColor())
audiQ3.setColor("Red")

# Function overridden in child class is called over here
print(audiQ3.showCar())