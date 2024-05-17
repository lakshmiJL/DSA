# Object Oriented Programming
#Focus on real life entities to write code

#Object - Any real Life entity represented in code
#for example - student, cars, fruits

#Class - Blueprint of an object
#(apple, banana, mango ) (objects) - > Fruits (class)

class Car:
    # attributes / properties of class
    def __init__(self, color, model, name, engine):
        self.color = color
        self.model = model
        self.name = name
        self.engine = engine
       
      #  Class Methods

      # Getters
    def get_name(self):
        return self.name

      # Setters
    def set_km(self, km):
        self.km = km

      # Custom Methods

    def showCar(self):
        print("Hello I own a  {}, {}, {}, {} car".format(self.name, self.model, self.color, self.engine))
        
c1 = Car("blue","Grand Vitara","Maruti Suzuki","Petrol Smart Hybrid")
c1.get_name()
c1.set_km(107)
c1.showCar()