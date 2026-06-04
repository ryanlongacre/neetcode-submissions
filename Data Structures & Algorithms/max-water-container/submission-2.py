class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_w = 0
        l = 0
        r = len(heights)-1

        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            if area > max_w:
                max_w = area
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_w
        