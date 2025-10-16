# String to Integer (atoi)

"""Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

    Whitespace: Ignore any leading whitespace (" ").

    Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.

    Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached.
    If no digits were read, then the result is 0.

    Rounding: If the integer is out of the 32-bit signed integer range [-2**31, 2**31 - 1], then round the integer to remain in the range.
    Specifically, integers less than -2**31 should be rounded to -2**31, and integers greater than 2**31 - 1 should be rounded to 2**31 - 1.

Return the integer as the final result."""


class Solution:
    def myAtoi(self, s):
        if not s:
            return 0

        i = 0
        n = len(s)

        # Skipping whitespaces
        while (
            i < n and s[i] == " "
        ):  # Ignore all leading whitespace characters, Advance the index i to the first non-whitespace character
            i += 1
        # Time Complexity: O(k) where k is the number of leading whitespace characters

        # Checking for the end
        if i == n:
            return 0

        # Checking for sign
        sign = 1  # Default to positive (sign = 1)
        # If + or - is found, set the sign and advance the index & Only the first sign is valid ("+-2" is invalid)
        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1
        # If no sign is present, proceed to the next step, Only advance the index when a sign is found

        # Constants for 32-Bit signed interger range
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        # Read digits and convert
        res = 0
        while i < n and s[i].isdigit():  # Continue reading digits and build the integer
            digit = int(s[i])
            res = (
                res * 10 + digit
            )  # To multiply by 10 for the next digit place and add the new digit

            # Check for overflow after each digit processing
            if sign * res <= INT_MIN:
                return INT_MIN
            if sign * res >= INT_MAX:
                return INT_MAX

            i += 1

        # Applying sign and return
        return res * sign


if __name__ == "__main__":
    obj = Solution()
    print(obj.myAtoi(s="42"))
