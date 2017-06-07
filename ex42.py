## Animal is-a object(yes, sort of confusing) look at the extra creddit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## super - builtin returns a proxy obhect that allows you to refer
        ##      parent class by 'super'
        ##  In Python, super() builtin-in has two major uses cases:
        ##      - Allows us to avoid using base class explicitly
        ##      - Working with Multiple Inheritance
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog(["Rover","Clover"])

## satan is-a Cat
satan = Cat({"Cat": "Satan", "Kitty": "Spawn"})

## mary is-a person
mary = Person(("Mary","Pary","Isabela"))

## mary has-a Satan
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frans has-a Rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## harry is a Halibut
harry = Halibut()

#Everything in Python is an object
"""
class A(object):

    def __init__(self):
        print("in here")
    def parrot(self, name):
        print("my parrot", name)

A.parrot(A(),"Otto")
"""
