"""An array is a data structure that stores elements of the same type in a contiguous block of memory. In an array, , of size ,
each memory location has some unique index,  (where ), that can be referenced as  or .

Your task is to reverse an array of integers."""


def rev(arr):
    arr = arr[::-1]
    return arr


print(rev(arr=[1, 4, 3, 2]))
