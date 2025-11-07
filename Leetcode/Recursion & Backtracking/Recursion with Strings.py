# String Reversal


def stringReversal(input_str: str) -> str:
    # What is the base case / When can I no longer continue?
    # Two Options for the base case a) reversing each letter or each letter reversed or one letter reversed itself
    # or the laziest way is the empty string
    # an empty string reversed is an empty string.
    if input_str == "":  # or len(input_str == 0)
        return ""

    # Now how do we consider to reach that base case?
    # What is the minimum amount of work to be done in each iteration? (Between each invocation, what's the small "unit" I can reverse)
    # to reach the final goal we have to modify single character and continue
    # so i pick a single char and then it will concathenated from the call stack in the reverse order
    return stringReversal(input_str[1:]) + input_str[0]
    # We are shrinking the string every time and storing single char at call stack and then the call stack returns the char reversed


if __name__ == "__main__":
    print(stringReversal(input_str="Hello"))
