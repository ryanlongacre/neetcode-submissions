class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        setNums = set(nums)
        longest = 0

        for num in setNums:
            if (num-1) not in setNums:
                length = 0
                while (num+length) in setNums:
                    length+=1
                longest = max(length, longest)
        return longest
        