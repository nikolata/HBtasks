def chain(iterable_1, iterable_2):
    try:
        iter(iterable_1)
        iter(iterable_2)
    except Exception:
        raise TypeError
    it_one = iterable_1
    it_two = iterable_2
    if isinstance(it_one, dict):
        it_one = list(it_one.values())
    if isinstance(it_two, dict):
        it_two = list(it_two.values())
    return list(it_one) + list(it_two)


print(list(chain(range(0, 4), range(4, 8))))
