# Object Oriented Programming
#Focus on real life entities to write code

#Object - Any real Life entity represented in code
#for example - student, cars, fruits

#Class - Blueprint of an object
#(apple, banana, mango ) (objects) - > Fruits (class)

class fruit:
    # attributes / properties of class
    def __init__(self, color, taste, shape, preference):
        self.color = color
        self.taste = taste
        self.shape = shape
        self.preference = preference
        self.sample = sample
      #  Class Methods

      # Getters
    def get_shape(self):
        return self.shape

      # Setters
    def set_shape(self, new_shape):
        self.shape = new_shape

      # Custom Methods
    def increase_preference(self):
        self.preference = self.preference + 1

    def showFruit(self):
        print("Hello I am a fruit with {}, {}, {}, {}".format(self.color, self.shape, self.taste, self.preference))


apple = fruit("red", "sour", "round",1)
apple.showFruit()
apple.increase_preference()

print(apple.get_shape())
apple.set_shape("sphere")
apple.showFruit()

banana = fruit("yellow", "sweet", "cylinder",2)
banana.showFruit()
banana.increase_preference()
banana.showFruit()