"""def banner(message, border='-'):
    print(border * len(message))
    print(message)
    print(border * len(message))


banner("Hi, my name is Python", "*")

count = 0


def show_count():
    print(count)


def set_count(c):
    global count  # Use it to refer global variables
    count = c


show_count()
set_count(5)
show_count()"""


# String formatting in Python
import math

pi = math.pi
print(f"The value of pi is {pi:.3f}")

print("The value of pi is {0:.3f}".format(pi))
