import sys
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 0, 55, 89]


def divlist(num):
    for i in a:
        try:
            b = num//int(i)
            print(f"{num} divided by {i} equals {b}")
        except ZeroDivisionError as e:
            print(f"{e!r}", file=sys.stderr)  # to flag the string as error need to use sys.stderr
            # raise


divlist(6)

# #  Importing platform specific error codes
# try:
#     import msvcrt
#
#     def getkey():
#         return msvcrt.getch()
#
# except ImportError:
#     import sys
#     import tty
#     import termios
#
#     def getkey():
#         fd = sys.stdin.fileno()
#         original_attributes = termios.tcgetattr(fd)
#         try:
#             tty.setraw(sys.stdin.fileno())
#             ch = sys.stdin.read(1)
#         finally:
#             termios.tcgetattr(fd, termios.TCSADRAIN, original_attributes)
#         return ch

# # Python code to illustrate working of try()

# def divide(x, y):
#     try:
#         # Floor Division : Gives only Fractional
#         # Part as Answer
#         result = x // y
#     except ZeroDivisionError:
#         print("Sorry ! You are dividing by zero ")
#     else:
#         print("Yeah ! Your answer is :", result)
#     finally:
#         # this block is always executed
#         # regardless of exception generation.
#         print('This is always executed')
#
#     # Look at parameters and note the working of Program
#
#
# divide(3, 2)
# divide(3, 0)
