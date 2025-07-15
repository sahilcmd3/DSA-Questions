# Simple array sum


def simpleSum(ar):
    sum = 0
    
    for i in range(len(ar)):
        sum += ar[i]

    return sum


if __name__ == "__main__":
    print(simpleSum(ar=[1, 2, 3, 4, 10, 11]))
