# if size of the array is 4 and number of elements is also 4 while appending the left element where would it go

# Using XOR bitwise
def find_missing_xor(arr):
    n = len(arr) + 1
    xor_all = 0
    xor_arr = 0

    # XOR all numbers from 1 to n
    for num in range(1, n + 1):
        xor_all ^= num

    # XOR all elements in the array
    for num in arr:
        xor_arr ^= num

    return xor_all ^ xor_arr  # Missing number
# Runs in O(n) time with O(1) space.

arr = [1, 2, 4, 5, 6]  # Missing number is 3
print("Missing number:", find_missing_xor(arr))



# Using hash set
def find_missing_numbers(arr, n):
    full_set = set(range(1, n + 1))
    arr_set = set(arr)
    return list(full_set - arr_set)
#Advantage: Handles multiple missing numbers easily

arr = [1, 2, 4, 6, 7, 9]  # Missing numbers are [3, 5, 8]
n = 9  # Range of numbers
print("Missing numbers:", find_missing_numbers(arr, n))



# Sorting and Checking
def find_missing_sorted(arr):
    arr.sort()
    for i in range(len(arr) - 1):
        if arr[i + 1] != arr[i] + 1:
            return arr[i] + 1
# Disadvantage: Requires sorting, making it O(n log n) time complexity.

arr = [1, 2, 4, 5, 6]
print("Missing number:", find_missing_sorted(arr))