class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        found = {}
        for i in range(len(nums)):
            if nums[i] in found:
                return True
            else:
                found[nums[i]] = i
                print(found)
        return False
         