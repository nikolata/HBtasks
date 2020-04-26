from decimal import *
from contextlib import contextmanager


'''
try:
    getcontext().prec = 3

    print(type(Decimal('asd') + Decimal('123')))
except Exception as exc:
    print(exc)


print(getcontext())
'''


@contextmanager
def change_precision(prec):
    try:
        getcontext().prec = prec
        yield
    except Exception as exc:
        if exc is not None:
            raise exc


class ChangePrecision:
    def __init__(self, prec):
        self.prec = prec

    def __enter__(self):
        getcontext().prec = self.prec
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass
