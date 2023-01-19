## Example-1

class Bike:
    name = ""
    gear = 0


bike1 = Bike()
bike1.name = "Yamaha"
bike1.gear = 6

print(f"{bike1.name} has {bike1.gear} gear")


## Example-2

class Employee:
    name = ""
    id = 0

E1 = Employee()
E2 = Employee()


E1.name = "Ram"
E1.id = 1234

E2.name = "Shayam"
E2.id = 6778


print(f"{E1.name} id number is {E1.id}")
print(f"{E2.name} id number is {E2.id}")


## We can also define a function inside a Python class. A Python Function defined inside a class is called a method.

class Room:
   #attribute
   length = 0.0
   breath = 0.0

   #method
   def calculate_area(self):
      print("Area of the room is = ", self.length*self.breath)


study_room = Room()
study_room.length = 3.0
study_room.breath = 4.0

study_room.calculate_area()