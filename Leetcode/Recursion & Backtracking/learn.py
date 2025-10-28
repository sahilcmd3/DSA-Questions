## Recursion

"""
> In most programming languages, a function can call another function. But a function can also call itself. Recursion is the technique
  where a function calls itself."""


# Example
def call_me():
    call_me


# > Here, the function calls itself, which is called recursion.
# > But "calling itself" is just a programmatic definition of recursion.

"""
> Recursion involves breaking down a problem into smaller pieces to the point that it cannot be further broken down. You solve the small 
  pieces and put them together to solve the overall problem."""


# > Technical Details of Recursion:

""" 
> Recursive Case: "Minimum work we can do." In the above example, asking the person in front of you how many people are ahead of them is 
  the least amount of work we can do.

> Base Case: "Condition where no work is required." In the above example, the person on the front of the line doesn't have to ask anything 
  so it is the condition where no work is required."""


# Example
# > Code for factorial of a number n * (n - 1) * (n - 2)!
def factorial(n):
    # No work required: Base Case
    if n == 1 or n == 0:
        return 1

    # Minimum amount of work: Recursive Case
    return n * factorial(n - 1)


print(
    factorial(n=5)
)  # Returns 120 which 5 * 4 * 3 * 2 * 1 (Base Case is activated at 1)

# Calls (Are stored in a stack {LIFO})
""" > 4th Call: 2 * (2 - 1 {Won't go further base condition reached where 1 returns 1}) [This gets popped from stack after base case fulfillment]
    > 3rd Call: 3 * (3 - 1) = 3 * 2 = 6 (popped)
    > 2nd Call: 4 * (4 - 1) = 4 * 6 = 24 (popped)
    > 1st Call: 5 * (5 - 1) = 5 * 24 = 120 (1st function call returning 120 to the initial function call and getting popped up from the stack)
    
    So the function finally returns the value 120 to the initial function call."""


# > Why do we need a base case?
"""
> In the above example we have used the stopping condition for the code. But what if we don't add a stopping condition or what if the function 
  we write never meets the stopping condition?"""

# > Will the code run forever?
""" > No - even if you don't terminate, your code won't run forever."""


# Example
def call():
    print("call")

    # Calling itself
    call()


""" > Output:
    > 5
    > 5
    > 5
    ... 
    RecursionError: maximum recursion depth exceeded."""

# > When a function is invoked, it is stored in a call stack.
""" 
> When a function called it gets stored in a call stack every time it is called it keeps getting in that stack. But the stack has limited space
  so there is no space left for function calling this condition is called STACK OVERFLOW. When the stack is full, it cannot accommodate any more 
  calls, causing a stack overflow error.
> Therefore, the base case is essential to prevent such errors and ensure the recursion terminates properly."""

# Example
# How to check for a palindrome?
"""
> Approach: Match the first and last letter of the string if they match remove them from the stack and match the inner ones keep doing it
  till we reach the middle element or all elements are eliminated.

> Minimum Work required or Recursive Case: Matching first and last letter and removing them.

> No Work required or Base Case: When there is one letter or no letters left at all, we can simply say it is a palindrome."""


def palindrome(s):
    # Base Case
    if len(s) == 0 or len(s) == 1:
        return True

    # Recursive Case {s[-1]: prints the last char "r" and so on like s[-2] prints "a"}
    if s[0] == s[-1]:
        return palindrome(
            s[1:-1]  # They matched then remove the first and last element {s[1:-1]: prints aceca}
        )

    return False


print(palindrome(s="racecar"))


# > When to use Recursion?
"""
> When code requires multiple loops and looks confusing and messy, recursion can offer a cleaner solution. Its use, however, 
  depends on the specific code and the type of data or data structure involved. For data structures like trees and graphs, recursion 
  can be particularly useful.

> Recursion can appear elegant and simple. But it often requires many steps to solve even simple problems due to the CPU overhead from 
  repeatedly adding methods to the stack. So before using it, make sure you carefully consider whether it's the right solution 
  for your problem."""
