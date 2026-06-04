class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetVals = {}
        for i in range(len(nums)):
            if ((target - nums[i]) in targetVals.keys()):
                return [targetVals[target - nums[i]], i]
            else:
                targetVals[nums[i]] = i