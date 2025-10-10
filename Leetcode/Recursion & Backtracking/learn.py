# Recursion is when a function calls itself until a specified condition is met

# without base case
def fun():
    count = 0
    print(count)
    fun()  # This is will continue endlessly 


count = 0

def fun():
    global count

    if count == 4:  # Base Condition (there can be more than one base condition)
        return
    
    print(count)
    count += 1

    fun()


# 1 to 5 name printing
def name():
    global count

    if count == 5:
        return
    
    print("Sahil")
    count += 1

    name()


# print n times
def ntimes(i, n):
    if i > n:
        return
    
    print(i)
    i += 1
    
    ntimes(i, n)


# Print linearly from 1 to N
def linear():
    global count

    if count == 10:
        return
    
    count += 1  # From 1 to 10 and for 0 to 9 count += 1 will be after print(count)
    print(count)

    linear()


# Print from N to 1
def revlinear(i, n):
    if i < n:
        return
    
# Write a recursive function that given an input n sums all the non negative integers
def sums(n):
    if n <= 0:
        return 0
    
    return n + sums(n - 1)


if __name__ == "__main__":
    # fun()
    # name()
    # linear()
    # rev_linear()
    # ntimes(i = 0, n = 6)
    print(sums(n=5))
