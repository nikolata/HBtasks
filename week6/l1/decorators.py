'''
def first(msg):
    print(msg)


first('hello')

second = first
second('world')


def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operate(func, x):
    result = func(x)
    return result


print(operate(inc, 5))

print(operate(dec, 5))


def is_called(msg):
    print('v is_called')

    def is_returned(msg):
        print(msg)
    print('v is_called')
    return is_returned


new = is_called('v called')
new('v returned')
'''

'''
def make_pretty(func):
    print('before pretty call')

    def inner():
        print('i got decorated')
        func()
    return inner


def ordinary():
    print('i am ordinary')


print(ordinary())
pretty = make_pretty(ordinary)
pretty()
'''


def smart_divide(func):
    def inner(a, b):
        print('i am going to divide ', a, ' and ', b)
        if b == 0:
            print('cant divide by 0')
            return
        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    return a / b


print(divide(4, 2))

print(divide(4, 0))


def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Hello")