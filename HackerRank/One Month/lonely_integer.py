# Given an array of integers, where all elements but one occur twice, find the unique element.


def lonelyInteger(a):
    return [i for i in a if a.count(i) == 1][0]


if __name__ == "__main__":
    print(lonelyInteger(a=[1, 2, 3, 4, 3, 2, 1]))
