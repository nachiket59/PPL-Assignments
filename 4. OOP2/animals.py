class Animal:
	def __init__(self, arg):
		self.__kingdom = 'animalia'
	def get_kingdom(self):
		print(self.__kingdom)		

class Trrestrial(Animal):
	def lives(self):
		print("Trrestrial animal lives on land")

class Arial(Animal):
	def lives(self):
		print("Arial animal lives in air")

class Aquatic(Animal):
	def lives(self):
		print("Aquatic animal lives in water")

class Mammal(Animal):
	def layeggs(self):
		return 'false'

class layer(Animal):
	def layeggs(self):
		return 'true'

class dog(Trrestrial,Mammal):
	def __init__(self):
		self._legs = 4;
		super().__init__(self)
	def get_legs(self):
		print("dog has "+str(self._legs)+" legs")

class crow(Arial,layer):
	def __init__(self):
		self._legs = 2;
		super().__init__(self)
	def get_legs(self):
		print("crow has "+ str(self._legs)+" legs")

class whale(Aquatic, Mammal):
	def __init__(self):
		self._legs = 0;
		super().__init__(self)
	def get_legs(self):
		print("crow has "+ str(self._legs)+" legs but has fins")

##driver program##
d = dog()
c = crow()
w = whale()
print("## dog's properties ##")
d.get_kingdom()
d.get_legs()
d.lives()
print("lay eggs? ",d.layeggs())
print("## crow's properties ##")
c.get_kingdom()
c.get_legs()
c.lives()
print("lay eggs? ",c.layeggs())
print("## whale's properties ##")
w.get_kingdom()
w.get_legs()
w.lives()
print("lay eggs? ",w.layeggs())
