# CRT PRACTICE QUESTIONS (First Set)

# Add Two Integers
"""def Sum(num1,num2):
    add = num1 + num2
    return add

ans = Sum(num1 = -10, num2 = 4)
print(ans)


# Convert Two Temperatures
def convert(Celsius):
    kelvin = celsius + 273.15
    fahrenheit = celsius * 1.80 + 32.00
    return [kelvin, fahrenheit]
    
ans = convert(celsius = 36.50)
print(ans)


# Smallest Even Multiple
def sem(n):
    if n % 2 == 0:
        return n
    else:
        return n * 2

ans = sem(n = 6)
print(ans)


# Alternating Digit Sum

Another approach
convert int to string
find length of the string
find odd, even sum
a-b/b-a depending on length

def ads(n): #aryan waali approach
    sum = 0
    while n:
        sum = (n % 10) - sum
        n //= 10
    return sum

ans = ads(n = 521)
print(ans)


# Palindrome
def palindrome(n):
    s = str(n)
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True

ans = palindrome(n = 121)
print(ans)"""

# Prime Number
# Time Complexity: O(root(n)/6)
"""def isprime(n):
    if n<=1:
        return False
    elif n<=3:
        return False
    elif n%2==0 or n%3==0:
        return False

    i=5
    while i*i<=n: # checking 6n+-1
        if n%i==0 or n%(i+2)==0:
            return False
        i+=6

    return True

ans=isprime(n=7)
print(ans)"""

#Reverse Digits
"""def revedigits(n):
    reverse_str = ""
    while n > 0:
        reverse_str += str(n % 10)
        n //= 10  # Right shift
    return int(reverse_str)

ans = revedigits(n=122)
print(ans)


# Armstrong Number
def armsnum(n):
    temp = n # Store the original number to compare later
    res = 0 # Variable to store the sum of the cubes of the digits

    while n != 0: # Loop to process each digit of the number
        digit = n % 10 # Get the last digit of the number
        res += digit ** len(n) # Add the cube of the digit to the result
        n //= 10 # Remove the last digit from the number

    if res == temp: # Check if the sum of cubes (res) is equal to the original number or not
        return True
    else:
        return False

ans=armsnum(n=153)
print(ans)"""


#armstrong till 10000
def armstrong(number):
    digits = [int(d) for d in str(number)]  # Converted num to string to iterate
    armstrong_sum = sum(d ** len(digits) for d in digits)  # sum of the power equivalent to no of digits in base
    return armstrong_sum == number


arms_numbers = []

for num in range(1, 10000):
    if armstrong(num):
        arms_numbers.append(num)

print(arms_numbers)