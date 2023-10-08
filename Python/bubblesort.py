"""Program to implement Bubble Sort in Python."""

a = [23, 21, 2, 32, 5, 80, 13, 1, 34, 55, 89]

print("Array before sorting " + str(a))


def bubble_sort(arr):
    c = len(arr)
    for i in range(0, c-1):

        for j in range(0, c-1-i):
            if arr[j+1] > arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]

    return arr


if __name__ == "__main__":
    bubble_sort(a)
    print("Array after sorting " + str(a))

