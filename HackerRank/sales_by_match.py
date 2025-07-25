# Sales by match

from collections import defaultdict


def sockMerchant(n, ar):
    p = defaultdict(bool)
    count = 0

    for num in ar:
        if not p[num]:
            p[num] = True
        else:
            count += 1
            p[num] = False

    return count


# Bitwise operator
"""understand how bitwise operators work. Here I've used:

    - The (<<) shift operator which shifts to the left the binary representation of the number placing zeroes in the right. In a base 10 
    number it's the same as multiplying by 2 n times.
    - The (&) AND operator which performs a AND logic operation in each bit of both operands. For example 0b00110 & 0b01100 = 0b00100 and 
    0b10000 & 0b00111 = 0b00000.
    - The (^= that is the same of a = a ^ b) XOR operator which, in a few words inverts the bits of a placed in the same position of the 1's 
    bits of b.

Now back to the question. The goal is to identify every repeated integer in the array. So for every integer I use the shift operator to 
create a binary representation of it (which I've called sock_hash) that contains only one 1 bit. Than the 5 becomes 100000, the 2 becomes 
100 and so on. With these representation I can "store" them in the accumulator integer using the XOR operator. But before it I check if 
there is another same sock_hash that was stored before which indicates it's a pair. And to conclude the "store" operation actually inverts 
that bit, which reset that bit to zero whenever a match is found. :)"""

def sockMerc(n, ar):
    accumulator = 0
    count = 0

    for sock in ar:
        sock_hash = 1 << sock
        if (accumulator & sock_hash):
            count += 1
        accumulator ^= sock_hash
    
    return count


if __name__ == "__main__":
    print(sockMerc(n=7, ar=[1, 2, 1, 2, 1, 3, 2]))
