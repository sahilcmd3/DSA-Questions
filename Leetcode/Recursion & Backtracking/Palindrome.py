# Palindrome


def palindrome(input_str: str) -> bool:
    if len(input_str) == 0 or len(input_str) == 1:
        return True

    if input_str[0] == input_str[-1]:
        return palindrome(input_str[1:-1])

    return False


if __name__ == "__main__":
    print(palindrome(input_str="AaaA"))
