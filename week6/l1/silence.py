def silence(file):
    def inner(func):
        def safe_error(*args):
            for arg in args:
                try:
                    func(arg)
                except Exception as exc:
                    with open(file, 'a') as f:
                        f.write("Calling `{}` raised an error - {}: '{}'. Provided arguments: {}".format(func.__name__,
                                                                                 type(exc).__name__, str(exc), *args))
                        f.write('\n')
        return safe_error
    return inner


@silence('errors.txt')
def foo(x):
    if x > 50:
        raise ValueError('Omg.')


foo(10)
foo(100)

# in errors.txt
# Calling `foo` raised an error - ValueError: 'Omg.'. Provided arguments: (100, )
