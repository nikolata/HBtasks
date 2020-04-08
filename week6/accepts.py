
def accepts(*args):
    acc_args = args

    def inner(func):
        def wrapper(*args):
            for i in range(len(acc_args)):
                if not isinstance(args[i], acc_args[i]):
                    raise TypeError("Argument {} of {} is not {}".format(args[i], func.__name__, acc_args[i].__name__))
            print(func(*args))
        return wrapper
    return inner


'''

@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)


say_hello(4)

'''


@accepts(str, int)
def deposit(name, money):
    print("{} sends {} $!".format(name, money))


deposit("Marto", 5)
