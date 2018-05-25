def myfunc(a,b):
    return sum((a,b)) * 0.05
print(myfunc(40,60))

def myfunc(*args):
    # *args return tuple of arguments
    print(type(args))

    for items in args:
        print(items)

    return sum(args) * 0.05

print(myfunc(40,60,100))

def myfunc(**kwargs):
    # **kwargs is a dictionary
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit: {}'.format(kwargs['fruit']))
    else:
        print('No')
myfunc(fruit = 'apple', veggie = 'lettuce' )

def myfunc(*args):
    for i in args:
        return "".join([x for x in i if (x.isupper() and (i.index(x)+1) % 2 is 0) or (x.islower() and (i.index(x)+1) % 3 is 0)])


print(myfunc('Anthropomorphism'))

def has_33(nums):
    find = [x for x, i in enumerate(nums) if i is 3]
    return [True for i in find if find.index(i)+1 < len(find) and (find[find.index(i)+1] - i) is 1]

print(has_33([1,3,1,3,3]))