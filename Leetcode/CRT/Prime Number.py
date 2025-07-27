#LEETCODE

# Time Complexity: O(root(n)/6)
def isprime(n):
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
print(ans)