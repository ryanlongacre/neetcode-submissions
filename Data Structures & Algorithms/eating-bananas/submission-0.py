class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        left = 1
        right = max(piles)

        lastWorked = 0

        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/mid)
            
            if hours > h:
                left = mid + 1
            elif hours <= h:
                right = mid - 1
                lastWorked = mid
        
        return lastWorked
        



        