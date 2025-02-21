#LEETCODE (medium)

"""You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve."""

#Greedy approach
#Time Complexity = O(n)
def max_profit(prices):
    profit_price_gain = [] # Empty list to store the profit
    for i in range(len(prices) - 1):
        if prices[i] < prices[i + 1]: #if price of i day is less than i+1 buy it and sell on the next better profit day
            profit_price_gain.append(prices[i + 1] - prices[i]) # add to the profit gained list
    return sum(profit_price_gain)


prices = [7, 1, 5, 3, 6, 4]
ans = max_profit(prices)
print(ans)
