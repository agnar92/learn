# Atribute and Class keyword
class Sample():
    pass



my_sample = Sample()
print(type(my_sample))


class Dog():

    def __init__(self, mybreed, name, spots):

        # self.atribute_name = arg
        self.breed = mybreed
        self.name = name

        # Expect boolean True/False
        self.sport = spots


my_dog = Dog(mybreed='lab', name='Sammy', spots=False)
print(my_dog)
print(my_dog.name)