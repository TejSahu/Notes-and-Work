"""def helloworld():
    print("Hello World!")

print(__name__)


id function is used to debug

a = 100
b = 200

print(id(a))
print(id(b))

b = 100
print(id(b))"""


a = [23, 1, 2, 32, 5, 80, 13, 21, 34, 55, 89]

n = 0
c = 0

while n < len(a):
    print('WHEN VALUE OF n ' + str(n))
    b = n
    while b != 0:
        # Code Here to sort
        c = a[b-1]
        print('Value of a[b] = ' + str(a[b]) + " Value of a[b-1] =" + str(a[b - 1]) + " Value of c " + str(c))
        if a[b-1] > a[b]:
            print("Swapping places")
            a[b-1] = a[b]
            a[b] = c
            print("After swapping")
            print("Value of a[b] = " + str(a[b]) + " Value of a[b-1] = " + str(a[b-1]) + " Value of c " + str(c))
        b = b - 1

    # adding value of n by 1
    n = n + 1
print(a)
