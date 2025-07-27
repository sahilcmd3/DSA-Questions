#LEETCODE (medium)

"""There are n students in a class numbered from 0 to n - 1. The teacher will give each student a problem starting
with the student number 0, then the student number 1, and so on until the teacher reaches the student number n - 1.
After that, the teacher will restart the process, starting with the student number 0 again.

You are given a 0-indexed integer array chalk and an integer k. There are initially k pieces of chalk. When the
student number i is given a problem to solve, they will use chalk[i] pieces of chalk to solve that problem.
However, if the current number of chalk pieces is strictly less than chalk[i], then the student number i will be
asked to replace the chalk.

Return the index of the student that will replace the chalk pieces.

Approach: First, calculate the total chalk used by all students in one complete round. Then, reduce k using the
modulus operation (k %= total) to determine the effective chalk count after accounting for all full rounds of
distribution. Finally, traverse the chalk array, subtracting each student's chalk usage from k until the remaining
chalk is insufficient for a student. This approach efficiently minimizes unnecessary iterations, making it optimal
even for large inputs."""


# Time Complexity: O(n)
def chalk_replacer(chalk, k):
    total = sum(chalk)
    k %= total
    i = 0

    while k >= chalk[i]:
        k -= chalk[i]
        i += 1

    return i


ans = chalk_replacer(chalk=[3, 4, 1, 2], k=25)
print(ans)