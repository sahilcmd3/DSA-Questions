# Minimum Time to Make Rope Colorful

"""Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help.
Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i]
is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

Return the minimum time Bob needs to make the rope colorful."""


class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        totalTime: int = 0
        i: int = 0
        j: int = 0

        while i < len(neededTime) and j < len(neededTime):
            curr_total: int = 0
            curr_max: int = 0
            while j < len(neededTime) and colors[i] == colors[j]:
                curr_total += neededTime[j]
                curr_max = max(curr_max, neededTime[j])
                j += 1

            totalTime += curr_total - curr_max
            i = j

        return totalTime


if __name__ == "__main__":
    obj = Solution()
    print(obj.minCost(colors="abaac", neededTime=[1, 2, 3, 4, 5]))
