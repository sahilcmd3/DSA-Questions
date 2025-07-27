# LEETCODE 375
"""We are playing the Guessing Game. The game will work as follows:
I pick a number between 1 and n.
You guess a number.
If you guess the right number, you win the game.
If you guess the wrong number, then I will tell you whether the number I picked is higher or lower, and you will continue guessing.
Every time you guess a wrong number x, you will pay x dollars. If you run out of money, you lose the game.
Given a particular n, return the minimum amount of money you need to guarantee a win regardless of what number I pick.
"""


def getmoney(n):
    left = 1
    right = n

    while left <= right:
        mid = (left + right) // 2
        res = guess(mid)  # Guess is the pre built api

        if res == 0:
            return mid
        elif res < 0:
            right = mid - 1
        else:
            left = mid + 1
