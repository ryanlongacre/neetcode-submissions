class Solution:
    def trap(self, height: List[int]) -> int:

        l = 0
        r = 1
        rollingSum = 0
        totalSum = 0
        while r < len(height):
            if height[r] >= height[l]:
                l = r
                r = r + 1
                totalSum += rollingSum
                rollingSum = 0
            else:
                rollingSum += height[l] - height[r]
                r += 1
        m = l
        rollingSum = 0

        r = len(height)-1
        l = len(height)-2

        while l >= m:
            if height[l] >= height[r]:
                r = l
                l = l - 1
                totalSum += rollingSum
                rollingSum = 0
            else:
                rollingSum += height[r] - height[l]
                l -= 1
        
        return totalSum

        