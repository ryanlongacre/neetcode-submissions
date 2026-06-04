class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0 for i in range(len(temperatures))]

        stack = [] # will append a tuple of (temp, index)
    

        for i, temp in enumerate(temperatures):
            while len(stack) != 0 and stack[-1][0] < temp:
                new_temp, new_index = stack.pop()
                res[new_index] = i - new_index
            stack.append([temp, i])
        for num, i in stack:
            res[i] = 0
        
        return res
        