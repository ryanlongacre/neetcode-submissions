class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = 0
        fast = 0

        slow = nums[slow]
        fast = nums[nums[fast]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        print(slow)
        
        secondSlow = 0
        while slow != secondSlow:
            slow = nums[slow]
            secondSlow = nums[secondSlow]
        
        return slow