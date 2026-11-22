class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)

        res = 0
        prefix = 0
        counts[0] += 1
        for num in nums:
            prefix += num
            res += counts[prefix - k]
            counts[prefix] += 1
        
        return res

