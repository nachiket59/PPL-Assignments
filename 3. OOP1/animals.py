#Parent Class
class Animal:
  def __init__(self):
    self._type = '' #Protected Member(Accessible to methods and derived classes)
    self.__kingdom = 'Animalia' #Private Member(Accessible to methods only)
  #Public Atrributes
  name = ''
  color = ''
  sound = ''
  #Method of the class which has access to private instance variable
  def get_kingdom(self):
    print('{}'.format(self.__kingdom))
  
  #Getter and setter functions to demonstrate abstraction   
  def set_name(self,name):
    self.name = name
  def set_color(self,color):
    self.color = color
  def set_sound(self,sound):
    self.sound = sound
  def get_name(self):
    print("Name is {}.".format(self.name))
  def get_color(self):
    print("{} is {} in color.".format(self.name,self.color))
  def get_sound(self):
    print("{} {}s".format(self.name,self.sound))

#Child class 1
class cat(Animal):
  def set_type(self):
    self._type = 'Cat' #Accessing a protected member via base class
    
  def get_type(self):
    # print(self.__kingdom) #Accessing a private member results in an error
    print('{} is a {}'.format(self.name,self._type))

#Child class 2
class dog(Animal):
  def set_type(self):
    self._type = 'Dog' #Accessing a protected member via base class

  def get_type(self):
    # print(self.__kingdom) #Accessing a private member results in an error
    print('{} is a {}'.format(self.name,self._type)) 

#Child class 3
class bat(Animal):
  def set_type(self):
    self._type = 'Bat' #Accessing a protected member via base class

  def get_type(self):
    # print(self.__kingdom) #Accessing a private member results in an error
    print('{} is a {}'.format(self.name,self._type))

#Child class 4
class donkey(Animal):
  def set_type(self):
    self._type = 'Donkey' #Accessing a protected member via base class

  def get_type(self):
    # print(self.__kingdom) #Accessing a private member results in an error
    print('{} is a {}'.format(self.name,self._type))

#Child class 5
class horse(Animal):
  def set_type(self):
    self._type = 'Horse' #Accessing a protected member via base class

  def get_type(self):
    # print(self.__kingdom) #Accessing a private member results in an error
    print('{} is a {}'.format(self.name,self._type))

#Child class 6
class cow(Animal):
  def set_type(self):
    self._type = 'Cow' #Accessing a protected member via base class

  def get_type(self):
    # print(self.__kingdom) #Accessing a private member results in an error
    print('{} is a {}'.format(self.name,self._type))

#Child class 7
class eagle(Animal):
  def set_type(self):
    self._type = 'Eagle' #Accessing a protected member via base class

  def get_type(self):
    # print(self.__kingdom) #Accessing a private member results in an error
    print('{} is a {}'.format(self.name,self._type))

#Child class 8
class tiger(Animal):
  def set_type(self):
    self._type = 'Tiger' #Accessing a protected member via base class

  def get_type(self):
    # print(self.__kingdom) #Accessing a private member results in an error
    print('{} is a {}'.format(self.name,self._type))

#Child class 9
class lion(Animal):
  def set_type(self):
    self._type = 'Lion' #Accessing a protected member via base class

  def get_type(self):
    # print(self.__kingdom) #Accessing a private member results in an error
    print('{} is a {}'.format(self.name,self._type))

#Child class 10
class cheetah(Animal):
  def set_type(self):
    self._type = 'Cheetah' #Accessing a protected member via base class

  def get_type(self):
    # print(self.__kingdom) #Accessing a private member results in an error
    print('{} is a {}'.format(self.name,self._type))

#driver program
lion = lion()
lion.set_type()
lion.set_name("tuffy")
lion.get_kingdom()
lion.get_type()         