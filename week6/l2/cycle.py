def cycle(rng):
    while True:
        for x in rng:
            yield x


endless = cycle(range(5))
print(endless)
for i in endless:
    print(i)
