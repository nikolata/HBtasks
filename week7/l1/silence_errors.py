from contextlib import contextmanager


class Silence_errors:
    def __init__(self, exc_type, msg=None):
        self.exc_type = exc_type
        self.msg = msg

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        same_exception_type = self.exc_type == exc_type
        correct_message = self.msg is None or str(exc_value) == self.msg

        return same_exception_type and correct_message


@contextmanager
def silence_errors(err_type, message=None):
    if not isinstance(err_type, type) or not isinstance(message, str) and message is not None:
        raise TypeError
    try:
        yield
    except Exception as exc:
        if err_type == exc.__class__ and message == str(exc):
            pass
        elif err_type == exc.__class__ and message is None and str(exc) is not None:
            pass
        else:
            raise err_type
