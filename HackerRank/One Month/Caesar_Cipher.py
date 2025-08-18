# Caesor Cipher

"""Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by
a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the
case of a rotation by 3, w, x, y and z would map to z, a, b and c."""


import string

LOWERCASE_ASCII = string.ascii_lowercase
UPPERCASE_ASCII = string.ascii_uppercase
ALPHABET_SIZE = 26


def caesar_cipher(s, k):
    encrypted = ""

    for char in s:
        if char in UPPERCASE_ASCII:
            encrypted += UPPERCASE_ASCII[(ord(char) - ord("A") + k) % ALPHABET_SIZE]
        elif char in LOWERCASE_ASCII:
            encrypted += LOWERCASE_ASCII[(ord(char) - ord("a") + k) % ALPHABET_SIZE]
        else:
            encrypted += char

    return encrypted


if __name__ == "__main__":
    print(caesar_cipher(s="There's-a-starman-waiting-in-the-sky", k=3))
