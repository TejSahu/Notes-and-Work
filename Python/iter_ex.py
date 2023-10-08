"""def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("Iterabale is empty")

print(first(["1st", "2nd", "3rd"]))
print(first({"1st", "2nd", "3rd"}))"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = list(reversed(a))


def zipex(one, two):
    for items in zip(one, two):
        print(items)


zipex(a, b)
"""def genex():
    yield a


g = genex()
print(next(g))"""
