class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        valid_arrays = []
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1

            while l < r:
                if nums[l] + nums[r] == nums[i] * -1:
                    valid_arrays.append([nums[l],nums[r],nums[i]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif nums[l] + nums[r] < nums[i] * -1:
                    l += 1
                else:
                    r -= 1
        return valid_arrays
