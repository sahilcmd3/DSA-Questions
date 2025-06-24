# LEETCODE 904


def totalFruit(fruits):
    n = len(fruits)
    left = 0
    ans = 0
    basket = {}

    for right in range(n):
        if fruits[right] not in basket:
            basket[fruits[right]] = 0
        basket[fruits[right]] += 1

        while len(basket) > 2:
            basket[fruits[left]] -= 1
            if (basket[fruits[left]]) == 0:
                del basket[fruits[left]]
            left += 1

        ans = max(ans, right - left + 1)

    return ans


print(totalFruit(fruits=[1, 2, 1]))
