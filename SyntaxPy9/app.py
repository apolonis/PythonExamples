class Person:
    def __init__(self,name):
        self.name = name

    def talk(self,name):
        print(f"{name} is talking")

person = Person("David")
person.talk(person.name)
# print(person.name)

person2 = Person("Ryan")
person2.talk(person2.name)