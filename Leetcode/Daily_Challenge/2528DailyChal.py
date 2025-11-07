# Maximize the Minimum Powered City

"""You are given a 0-indexed integer array stations of length n, where stations[i] represents the number of power stations in the ith city.

Each power station can provide power to every city in a fixed range. In other words, if the range is denoted by r, then a power station
at city i can provide power to all cities j such that |i - j| <= r and 0 <= i, j <= n - 1.

    Note that |x| denotes absolute value. For example, |7 - 5| = 2 and |3 - 10| = 7.

The power of a city is the total number of power stations it is being provided power from.

The government has sanctioned building k more power stations, each of which can be built in any city, and have the same range as the
pre-existing ones.

Given the two integers r and k, return the maximum possible minimum power of a city, if the additional power stations are built optimally.

Note that you can build the k power stations in multiple cities."""

from itertools import accumulate


# O(N∗Log(M)) Where N Is The Length Of Stations And M Is The Search Space For The Answer
class Solution:
    def check(
        self, mid: int, df: list[int], k: int, r: int, stations: list[int]
    ) -> bool:
        n = len(stations)
        diff = df[:]
        curr, cnt = 0, 0

        for i in range(n):
            curr += diff[i]
            if curr < mid:
                need = mid - curr
                cnt += need
                if cnt > k:
                    return False

                curr = mid
                diff[min(n - 1, i + 2 * r) + 1] -= need

        return True

    def maxPower(self, stations: list[int], r: int, k: int) -> int:
        n = len(stations)
        df = [0] * (n + 5)

        for i, j in enumerate(stations):
            df[max(0, i - r)] += j
            df[min(n - 1, i + r) + 1] -= j

        lo, hi = min(accumulate(df[:n])), 2 * 10**10

        while lo < hi:
            mid = (lo + hi + 1) >> 1

            if self.check(mid, df, k, r, stations):
                lo = mid
            else:
                hi = mid - 1

        return lo


if __name__ == "__main__":
    obj = Solution()
    print(obj.maxPower(stations=[1, 2, 4, 5, 0], r=1, k=2))
