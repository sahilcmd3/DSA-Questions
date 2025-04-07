#LEETCODE

"""You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a
different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0"""

"""The solution we previously discussed for finding the maximum profit by buying and selling a stock already 
uses a greedy algorithm. In a greedy algorithm, we make a series of choices, 
each of which looks best at the moment, with the hope that the overall result will be optimal."""


#Time Complexity: O(n)
def max_profit(prices):
    if not prices:
        return 0

    min_price = float('inf')  #is initialized to infinity to ensure that any price we encounter will be lower.
    max_profit = 0  #is initialized to 0 to store the maximum profit found.

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit


prices = [7, 6, 4, 3, 1]
sol = max_profit(prices)
print(sol)