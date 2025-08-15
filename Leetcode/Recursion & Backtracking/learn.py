# Recursion is when a function calls itself until a specified condition is met

"""
def fun():
    count = 0
    print(count)
    fun()  # This is will continue endlessly 
"""

count = 0


def fun():
    global count
    if count == 4:  # Base Condition (there can be more than one base condition)
        return
    print(count)
    count += 1
    fun()


if __name__ == "__main__":
    fun()
