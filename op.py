#          ---------    PYTHON OOPS    ---------

# A practice code 
class Car(): #parent class
  # Constructors are used to initialize the object. Like methods, a constructor also contains 
	#  a collection of statements(i.e. instructions) that are executed at the time of Object creation.
	car_type = 'Sedan'  #class attribute - outside constructor method
	def __init__(self,name,mileage,color): #__init__() method is aka constructor method
	# the first parameter of this method has to be self. Then only will the rest of the parameters come
		self.name = name #instance attribute - inside constructor method
		self.mileage = mileage #instance attribute - inside constructor method
		self._color = color # protected variable | Encapsulation
	# Methods are the functions that we use to describe the behavior of the objects.
	def description(self):
		return f"The {self.name} car gives the mileage of {self.mileage}km/l."
	def max_speed(self,speed):
		return f"The {self.name} runs at max speed of {speed}km/hr."
	# The methods defined inside a class other than the constructor method are known as the instance methods.
	class BMW(Car): #child class
		pass
	# Inheritance exapmples above and below
	class Audi(Car): #child class
		def audi_desc(self):
			return "This is the description method of class Audi."

# Polymorphism
class Audi:
  def description(self):
    print("This the description function of class AUDI.")
class BMW:
  def description(self):
    print("This the description function of class BMW.")
audi = Audi()
bmw = BMW()
for car in (audi,bmw):
	car.description()

# data abstraction is done by using inheritance.
from abc import ABC, abstractmethod
class Car(ABC):
    def __init__(self,name):
        self.name = name
    def description(self):
        print("This the description function of class car.")
    @abstractmethod
    def price(self,x):
        pass
class new(Car):
    def price(self,x):
        print(f"The {self.name}'s price is {x} lakhs.")
obj = new("Honda City")
obj.description()
obj.price(25)
