
# LEGB Rule
x = 25

def printer():
    x = 50
    return x

print(x)
print(printer())

# local
lambda num: num**2

# enclosure
name = 'this'
def greet():
    name = 'Sammy'

    def hello():
        print('hello'+name)

    hello()
greet()