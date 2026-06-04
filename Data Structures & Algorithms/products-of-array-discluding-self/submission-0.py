class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = [1] * len(nums)

        #prefix run through
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix = nums[i] * prefix
        
        postfix = 1
        for i in range(len(nums)):
            output[len(nums)-i-1] *= postfix
            postfix = nums[len(nums)-i-1] * postfix
        
        return output

        