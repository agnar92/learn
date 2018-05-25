#inherit

class Animal():

    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am a animal")

    def eat(self):
        print("I am eating")


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def who_am_i(self):
        print("I am a Dog")



myanimal = Animal()
myanimal.eat()

mydog = Dog()
mydog.who_am_i()
print()

# polymorphism


class Cat():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return  self.name + " says may"


class Owl():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says whoho"



niko = Cat('Niko')
felix = Owl('Felix')

print(niko.speak())
print(felix.speak())

for pet in [niko, felix]:
    print(type(pet))
    print(pet.speak())

print()


def pet_speek(pet):
    print(pet.speak())

pet_speek(niko)
pet_speek(felix)


class Animal():

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implemetne this abstract methode")

    def bark(self):
        pass

class Dog(Animal):

    def speak(self):
        return self.name + ' say woof'

    def bark(self):
        return self.name + ' bark'



dog = Dog('Felix')
print(dog.speak())
print(dog.bark())