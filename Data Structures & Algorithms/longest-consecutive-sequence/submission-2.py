class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        subs = set(nums)
        lengths = []
        for num in nums:
            if num - 1 in subs:
                continue
            k = 1
            while num + k in subs:
                k += 1
            lengths.append(k)
        return max(lengths)
        