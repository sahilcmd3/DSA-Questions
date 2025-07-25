# Comparison Sorting
"""Quicksort usually has a running time of nlog(n), but is there an algorithm that can sort even faster? In general, this is not possible.
Most sorting algorithms are comparison sorts, i.e. they sort a list just by comparing the elements to one another. A comparison sort
algorithm cannot beat nlog(n) (worst-case) running time, since nlog(n) represents the minimum number of comparisons needed to know where to
place each element."""

# Alternative Sorting
"""Another sorting method, the counting sort, does not require comparison. Instead, you create an integer array whose index range covers the 
entire range of values in your array to sort. Each time a value occurs in the original array, you increment the counter at that index. At the 
end, run through your counting array, printing the value of each non-zero valued index that number of times."""


def countingSort(arr):
    result = [0] * 100

    for i in arr:
        result[i] += 1

    return result


if __name__ == "__main__":
    print(countingSort(arr=[1, 1, 3, 2, 1]))

# returned a freq array with range till 100 and freq count of each element from the original array at respective positions
