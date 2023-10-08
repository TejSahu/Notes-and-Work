names = ['Tej Sahu', 'Namrata Bahu', 'Bablu Ambast']

a = sorted(names, key=lambda name: name.split()[-1])
print(a)

b = lambda out: print(out)

# __call__() method examples below


"""import socket


class Resolver:

    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]

    def clear(self):
        self._cache.clear()

    def has_host(self, host):
        return host in self._cache"""

# mutable and immutable example

"""def sequence_class(immutable):
    if immutable:
        cls = tuple
    else:
        cls = list

    return cls"""
