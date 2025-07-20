"""A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in
the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.
"""


def pangrams(s):
    alphabet = {}

    for i in s.lower():
        if i.isalpha() and i in alphabet:
            alphabet[i] += 1
        elif i.isalpha() and i not in alphabet:
            alphabet[i] = 0

    if len(alphabet) == 26:
        return "pangram"
    else:
        return "not pangram"


if __name__ == "__main__":
    print(pangrams(s="We promptly judged antique ivory buckles for the next prize"))
