class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}
        finalList = []
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        bucket = [[] for i in range(len(nums))]

        for key,val in counts.items():
            bucket[val-1].append(key)
        
        for i in range(len(nums)-1, -1, -1):
            if k <= 0:
                return finalList
            if len(bucket[i]) != 0:
                k -= len(bucket[i])
                finalList.extend(bucket[i])
        return finalList

        