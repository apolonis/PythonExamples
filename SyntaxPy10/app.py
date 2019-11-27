
# INHERITANCE
class Animal:
    def walk(self):
        print("Walk")

class Dog(Animal):
    pass
    def bark(self):
        print("Bark")

class Cat(Animal):
    pass
    def meow(self):
        print("Meow")

dog = Dog()
cat = Cat()

dog.walk()
cat.walk()

dog.bark()
cat.meow()