def f():
    yield 1
    yield 2
    yield 3
r1 = f()

# r1
r1.__next__()


