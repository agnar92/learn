# lambda anonymous finction

def square(num):
    return num**2

my_nums = [1,2,3,4,5]

# map
for item in map(square, my_nums):
    print(item)

print(list(map(square,my_nums)))


def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

name = ['Andy', 'Eve', 'Sally']
print(list(map(splicer, name)))


def check_even(num):
    return num%2 is 0

mynums = [1,2,3,4,5,6]

print(list(filter(check_even, mynums))) # return values from mynums that are true form result function
print(list(map(check_even, mynums))) # return result from function for mynums

print(lambda num: num **2)

print(list(map(lambda num: num**2, mynums)))
print(list(filter(lambda num: num%2 is 0, mynums)))

print(list(map(lambda x: x[::-1], name)))


