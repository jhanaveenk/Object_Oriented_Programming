##  __init__() is the constructor function that is called whenever a new object of that class is instantiated.

class Bike:
   def __init__(self, name, gear):
      self.name = name
      self.gear = gear


b = Bike('yamaha', 6)

setattr(b , "gear", 9)

print(getattr(b , "name"), getattr(b, "gear"))