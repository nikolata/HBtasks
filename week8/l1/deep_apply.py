from random import randint
import ipdb


data = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'V': {
        'P': 5,
        'M': 6,
        'N': 7
    }
}


def foo():
    return randint(1, 1000)


def deep_apply(func, data):
    visited = []

    def inner(func, data, visited, key):
        if key not in visited:
            visited.append(key)
            if isinstance(data[key], dict):
                inner(func, data[key], visited, list(data[key].keys())[0])
            else:
                data[key] = func()
            for neigh in data:
                ipdb.set_trace()
                inner(func, data, visited, neigh)
            return data
    return inner(func, data, visited, list(data.keys())[0])


result = deep_apply(foo, data)
print(result)
