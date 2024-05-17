# Class User to explain the concept of hidden attribute 

class User:

    # hidden variable
     __password = "Abc@123"

    def __init__(self, name, email, username):
        self.name = name
        self.email = email
        self.username = username
        
    def getPassword(self):
        return self.__password

    def setPassword(self):
        old_password = input("Enter your old password - ")
        if old_password == self.__password:
          new_password = input("Enter your new password - ")
          self.__password = new_password

        else:
          print("Please enter the correct password.")

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
        



# Concept of hidden variable
pulkit = User("Pulkit", "pulkit.jetlearn@gmail.com", "major_pulkit")
# attribute is accessible from code
print(pulkit.name)
# hidden password is not accessible
print(pulkit.__password)
print(pulkit.getPassword())
pulkit.setPassword()


# Concept of Inheritance

audiQ3 = SUV("Audi", "Q3", "Disel", "White", "Automatic", True)

# Inherited from class Car
print(audiQ3.getColor())
audiQ3.setColor("Red")

# Function overridden in child class is called over here
print(audiQ3.showCar())