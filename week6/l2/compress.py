def compress(iterable, mask):
    for i in range(len(iterable)):
        if mask[i]:
            yield iterable[i]


print(list(compress(["Ivo", "Rado", "Panda", 'Gucci', 'Mane'], [False, False, True, False, True])))
