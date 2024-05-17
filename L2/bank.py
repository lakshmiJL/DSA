import datetime

class Person():
    #constructor
    def __init__(self, name):
        self.name = name
        try:
            lastBlank = name.rindex(" ")
            self.lastname = name[lastBlank+1: ]
        except:
            self.lastname = name
        self.birthdate = None

    #getters
    def getName(self):
        return self.name
    def getLastName(self):
        return self.lastname
    def getAge(self):
        if self.birthdate == None:
            raise ValueError("Birthdate not set for" + self.name)
        #print(self.birthdate)
        #print(datetime.date.today())
        return(datetime.date.today() - self.birthdate).days
    
    #setters
    def setBirthdate(self, bday):
        self.birthdate = bday
    
    def __lt__(self, other):
        #compare the names of the persons
        if self.lastname == other.lastname:
            return self.name < other.name
        return self.lastname < other.lastname

    def __str__(self):
        return self.name


sa = Person("Surabhi Ahuja")
bw = Person("Bruce Wayne")

print(bw)
sa.setBirthdate(datetime.date(1982,10,2))
print(sa.getAge())

people=[bw,sa]
for p in people:
    print(p)

print(sa < bw)
print("Sorting the list")
people.sort()
for p in people:
    print(p)


#Starting to make subclasses
class BankPerson(Person):#isA relationship
    nextId = 0 
    def __init__(self,name):
        Person.__init__(self,name)
        self.id = BankPerson.nextId#nextId is not a instance variable - rather it is a class variable
        BankPerson.nextId += 1

    def getId(self):
        return self.id

    #overriding the comparison function
    def __lt__(self, other):
        print("i am in the sub class")
        return self.id < other.id

print("Testing the BankPerson class")
bp1 = BankPerson("Surabhi Patil")
print(bp1)#calling the __str__ of the Person class
print("Id of Surabhi Ahuja is", bp1.getId())
bp2 = BankPerson("Captain America")
print("Id of Captain America is", bp2.getId())
        

print(bp2 < bp1)
print("Comparing a Person with a bankPerson")
print(bw < bp2)
print("Comparing BankPerson with a Person")
print(bp2 < bw)