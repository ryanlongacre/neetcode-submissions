class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        stack = [(0, heights[0])]
        maxArea = 0
        for i in range(1, len(heights)):
            c = i
            while len(stack) != 0 and stack[-1][1] > heights[i]:
                maxArea = max(maxArea, (i - stack[-1][0]) * stack[-1][1])
                c = stack[-1][0]
                stack.pop()
            stack.append((c, heights[i]))


        for pair in stack:
            maxArea = max(maxArea, (len(heights) - pair[0]) * pair[1])

        return maxArea            
        