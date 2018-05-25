class Dog():

    # Class object attribute
    # same for any instacne of a class
    species = 'mammal'

    def __init__(self, mybreed, name):

        # self.atribute_name = arg
        self.breed = mybreed
        self.name = name

    # Operation/Actions ---> methods
    def bark(self, number):
        print('Woof My name is {} and the number is {}'.format(self.name, number))


my_dog = Dog(mybreed='Lab', name='Sammy')
print(my_dog)
print(my_dog.name)
print(my_dog.species)
my_dog.bark(2)
print()


class Circle():

    # Class object attribute
    pi = 3.14

    def __init__(self, radius=1):

        self.radius = radius
        self.area = radius * radius * Circle.pi

    def get_circumference(self):
        return self.radius * self.pi *2


my_circle = Circle(30)
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.area)
print(my_circle.get_circumference())
