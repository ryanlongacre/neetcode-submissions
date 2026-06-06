class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums2, nums1 = nums1, nums2

        totalLength = len(nums1) + len(nums2)
        half = (totalLength + 1) // 2
        

        l = 0
        r = len(nums1)

        while l <= r:

            mid = (l + r) // 2

            valL = nums1[mid-1] if mid != 0 else -math.inf
            valR = nums1[mid] if mid != len(nums1) else math.inf
            
            amtRemaining = half - mid

            val2L = nums2[amtRemaining-1] if amtRemaining != 0 else -math.inf
            val2R = nums2[amtRemaining] if amtRemaining != len(nums2) else math.inf
            
            if valL > val2R:
                r = mid -1
            elif valR < val2L: 
                l = mid + 1
            else:
                if totalLength % 2 == 0:
                    return (max(valL, val2L) + min(valR, val2R)) / 2
                else:
                    return max(valL, val2L)
        
        
            

            
            
        
