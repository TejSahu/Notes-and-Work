# Sort array from so that 1s are in left and Zeros are in right
a = [0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1]


def zerosort(arr):
    c = len(arr)
    for i in range(0, c - 1):

        for j in range(i, c - 1 - i):
            if arr[j + 1] == 0 and arr[j] == 1:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]

    return arr


if __name__ == "__main__":
    print(zerosort(a))
