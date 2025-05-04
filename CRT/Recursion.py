"""Recursion is calling a function in the function itself. reduces code complexity and number of iterations"""

# Factorial
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

print("Factorial:", fact(n=5), "\n")


# Sum of all elements of array
def sumoarray(n, index=0):
    if index == len(n):
        return 0
    else:
        return n[index] + sumoarray(n, index + 1)

print("Sum of array:", sumoarray(n=[1, 2, 3, 4, 5]), "\n")


# Print no.s from 1 to 10
def printnum(n):
    if n > 10:  # or n<1 (for reverse print)
        print("#")
        return
    if n == 10:
        print(n, end="")
    else:
        print(n, end=" ")
    printnum(n + 1)  # or printnum(n-1)

printnum(1)  # or printnum(10)

print()


# Types of recursion
"""Plain and composite recursion are two different ways of structuring recursive functions.

### Plain Recursion
- In plain recursion, a function calls itself only once per recursive step.
- This is the simplest form of recursion, where each call reduces the problem size by a single step.

#### Example (Factorial Calculation)
```cpp
int factorial(int n) {
    if (n == 0) return 1;  // Base case
    return n * factorial(n - 1);  // Recursive call
}
```
- Here, `factorial(n)` calls itself once in each step.
- The recursion depth is linear, meaning it follows a single chain of function calls.
---

### Composite Recursion
- In composite recursion, a function calls itself multiple times within a single recursive step.
- This often leads to a tree-like recursive structure, where each call branches into multiple recursive calls.

#### Example (Fibonacci Sequence)
```cpp
int fibonacci(int n) {
    if (n <= 1) return n;  // Base case
    return fibonacci(n - 1) + fibonacci(n - 2);  // Two recursive calls
}
```
- Here, `fibonacci(n)` calls itself twice in each step.
- The recursion depth grows exponentially, forming a tree structure.
---

### Key Differences
|        Feature           | Plain Recursion |          Composite Recursion         |
|--------------------------|-----------------|--------------------------------------|
| Number of Calls per Step |        1        |             More than 1              |
| Structure                |     Linear      |              Tree-like               |
| Efficiency               |  Usually better | Can be inefficient (e.g., Fibonacci) |
| Example                  |    Factorial    |              Fibonacci               |
"""


"""def com_print(n):
    if n>10:
        return

    print(n)

    com_print(n+1)
    com_print(n+1)

com_print(1)"""


# Fibonacci series
"""Used for continuous converging pendulum eg, 1.66, 1.6 , 1.625, 1.615 (mid is 1.620)"""
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(n = 5), "\n")


# Binary search using recursion
def binarysearch(arr, low, high, target):
    if high >= low:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            return binarysearch(arr, low, mid - 1, target)

        else:
            return binarysearch(arr, mid + 1, high, target)

    else:
        return -1

arr = [2, 3, 4, 10, 40]
target = 10
result = binarysearch(arr, 0, len(arr) - 1, target)
print(result, "\n")