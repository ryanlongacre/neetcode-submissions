class Solution:
    def trap(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]

        ret = 0

        while l < r:
            if maxL < maxR:
                l += 1
                ret += max(0, maxL - height[l])
                maxL = max(maxL, height[l])
            else:
                r -= 1
                ret += max(0, maxR - height[r])
                maxR = max(maxR, height[r])
        return ret
            

        