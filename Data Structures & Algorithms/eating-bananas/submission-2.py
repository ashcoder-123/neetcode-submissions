from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(speed):
            totalHours = 0

            for pile in piles:
                totalHours += ceil(pile / speed)

            return totalHours <= h
        l = 1
        r = max(piles)
        while l < r:
            mid = (l+r)//2
            if canFinish(mid):
                r = mid
            else:
                l = mid+1
        return l     