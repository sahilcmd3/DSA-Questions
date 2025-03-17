#LEETCODE (Medium)

"""Seven different symbols represent Roman numerals with the following values:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000

Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting
a decimal place value into a Roman numeral has the following rules:

If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input,
append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol,
for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms
are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).

Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot
append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.

Given an integer, convert it to a Roman numeral."""


def int_to_roman(num):
    num_map = {
        1: "I",
        5: "V", 4: "IV",
        10: "X", 9: "IX",
        50: "L", 40: "XL",
        100: "C", 90: "XC",
        500: "D", 400: "CD",
        1000: "M", 900: "CM",
    }

    r = ''

    for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
        # If n in list then add the roman value to result variable
        while n <= num:
            r += num_map[n]
            num -= n

    return r


num = 3749
ans = int_to_roman(num)
print(ans)