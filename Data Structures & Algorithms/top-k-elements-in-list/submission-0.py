class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        heap = []
        for c in counts:
            heapq.heappush(heap, (counts[c], c))
            if len(heap) > k:
                heapq.heappop(heap)
        finalList = []
        for i in range(k):
            finalList.append(heapq.heappop(heap)[1])

        return finalList
        