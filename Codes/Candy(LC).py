#LEETCODE (Hard)

"""There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
You are giving candies to these children subjected to the following requirements:
    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.
    Return the minimum number of candies you need to have to distribute the candies to the children."""


#Two pass greedy approach
#Time complexity: O(n)
#Space complexity: O(n)

def candy(ratings):

    n = len(ratings)
    candies = [1] * n

    for child in range(1, n):  #left to right
        if ratings[child] > ratings[child - 1]:  #checking left side
            candies[child] = candies[child - 1] + 1

    for child in range(n - 2, -1, -1):  #right to left checking right side
        if ratings[child] > ratings[child + 1]:
            candies[child] = max(candies[child], candies[child + 1] + 1)

    return sum(candies)


ratings = [20000, 20000, 16001, 16001, 16002, 16002, 16003, 16003, 16004, 16004, 16005, 16005, 16006, 16006, 16007, 16007, 16008, 16008, 16009, 16009, 16010, 16010, 16011, 16011, 16012, 16012, 16013, 16013, 16014, 16014, 16015, 16015, 16016, 16016, 16017, 16017, 16018, 16018, 16019, 16019, 16020, 16020, 16021, 16021, 16022, 16022, 16023, 16023, 16024, 16024]
ans = candy(ratings)
print(ans)


#One-Pass greedy approach: Up-Down-Peek Method
#Time complexity: O(n)
#space complexity: O(1)
"""class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        
        ret, up, down, peak = 1, 0, 0, 0
        
        for prev, curr in zip(ratings[:-1], ratings[1:]):
            if prev < curr:
                up, down, peak = up + 1, 0, up + 1
                ret += 1 + up
            elif prev == curr:
                up = down = peak = 0
                ret += 1
            else:
                up, down = 0, down + 1
                ret += 1 + down - int(peak >= down)
        
        return ret

for explanation check theory of greedy"""