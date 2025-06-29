# Password Cracker


import sys

sys.setrecursionlimit(10000)


def passwordCracker(passwords, loginAttempt):
    passwords.sort(key=len, reverse=True)
    word_set = set(passwords)
    memo = {}

    def dfs(attempt):
        if attempt in memo:
            return memo[attempt]
        if attempt == "":
            return []

        for word in word_set:
            if attempt.startswith(word):
                result = dfs(attempt[len(word) :])
                if result is not None:
                    memo[attempt] = [word] + result
                    return memo[attempt]

        memo[attempt] = None
        return None

    result = dfs(loginAttempt)
    return " ".join(result) if result else "WRONG PASSWORD"


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        passwords = input().strip().split()
        loginAttempt = input().strip()
        print(passwordCracker(passwords, loginAttempt))
