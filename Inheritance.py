class Animal:
    def eat(self):
        print(" I Eat")

    def sleep(self):
        print("I only sleep")


class Dog(Animal):
    def bark(self):
        print("I Bark")


dog=Dog()

dog.eat()
dog.sleep()
dog.bark()