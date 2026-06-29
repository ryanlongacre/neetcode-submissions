class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        sol = []

        for i, num in enumerate(nums):

            #only positive numbers will never be 0
            if num > 0:
                break
            
            #if we already did solved for the same number, won't change anything
            if i > 0 and num == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[l] + nums[r] + num
                if total == 0:
                    sol.append([nums[l], nums[r], num])
                    l += 1
                    r -= 1
                    #make sure we don't repeat for any specific number
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return sol