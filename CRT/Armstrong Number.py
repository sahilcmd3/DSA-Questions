#LEETCODE

def armsnum(n):
    temp = n # Store the original number to compare later
    res = 0 # Variable to store the sum of the cubes of the digits

    while n != 0: # Loop to process each digit of the number
        digit = n % 10 # Get the last digit of the number
        res += digit **3 # Add the cube of the digit to the result
        n //= 10 # Remove the last digit from the number

    if res == temp: # Check if the sum of cubes (res) is equal to the original number or not
        return True
    else:
        return False

ans=armsnum(n=153)
print(ans)


#armstrong till 10000
"""def armstrong(number):
    digits = [int(d) for d in str(number)]  # Converted num to string to iterate
    armstrong_sum = sum(d ** len(digits) for d in digits)  # sum of the power equivalent to no of digits in base
    return armstrong_sum == number

arms_numbers = []

for num in range(1, 10000):
    if armstrong(num):
        arms_numbers.append(num)

print(arms_numbers)"""