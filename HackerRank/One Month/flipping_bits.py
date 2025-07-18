# You will be given a list of 32 bit unsigned integers. Flip all the bits (1 -> 0 and 0 -> 1) and return the result as an unsigned integer.


def flippingbits(n):
    l = format(n, '032b')
    m = []
    
    for i in range(len(l)):
        m.append(1 - int(l[i]))
    
    sum = 0
    for i in range(len(m)):
        sum += int(m[i]) * (2 ** (31 - i))
    
    return sum


if __name__ == "__main__":
    print(flippingbits(n=9))
