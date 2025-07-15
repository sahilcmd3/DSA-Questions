# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each
# fraction on a new line with places after the decimal.
# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to
# are acceptable.


def plus_minus(arr):
    plus_count = 0
    minus_count = 0
    zero_count = 0

    for i in arr:
        if i > 0:
            plus_count += 1
        elif i < 0:
            minus_count += 1
        else:
            zero_count += 1

    print(round(plus_count / len(arr), 6))
    print(round(minus_count / len(arr), 6))
    print(round(zero_count / len(arr), 6))


if __name__ == "__main__":
    plus_minus(arr=[1, 1, 0, -1, -1])
