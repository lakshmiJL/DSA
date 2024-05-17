class ComplexNumber :
    #a constructor for our class
    #special method
    def __init__(self, r=0, i=0):
        #print("Constructing the class")
        self.real =  r
        self.imag = i
        
    def display(self):
        print (str(self.real) + "+" +"i" + str(self.imag))
    
    #str function - if i want to print my objects - special method
    def __str__(self):
        if self.imag < 0 :
            displayStr = str(self.real) + " - " +"i" + str(-self.imag)
        else:
            displayStr = str(self.real) + " + " +"i" + str(self.imag)
        return displayStr

    def conjugate(myself):
        return ComplexNumber(myself.real, -myself.imag)
        
    
z1 = ComplexNumber()#the constructor will get called on its own
z2 = ComplexNumber(2.0, 3.5)

#z1.display()
z2.real = 2.0
z2.imag = 3.5
#z2.display()

z3 = z2.conjugate()
print(z3)
help(ComplexNumber)
