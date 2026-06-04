class Solution:
    def trap(self, height: List[int]) -> int:

        totalSum = 0
        l = 0
        r = len(height) - 1

        if not height:
            return 0
        
        maxL, maxR = height[l], height[r]

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                totalSum += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                totalSum += maxR - height[r]
        return totalSum


        