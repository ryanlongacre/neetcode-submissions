class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        l = 0
        r = len(nums1)

        mid = -1
        amtRemaining = -1
        valL = -math.inf
        valR = math.inf
        val2L = -math.inf
        val2R = math.inf

        while l <= r:
            mid = (l + r) // 2

            if mid == 0:
                valL = -math.inf
            else:
                valL = nums1[mid-1]
            
            if mid == len(nums1):
                valR = math.inf
            else:
                valR = nums1[mid]

            amtRemaining = ((len(nums2) + len(nums1) + 1) // 2) - mid

            if amtRemaining == 0:
                val2L = -math.inf
            else:
                val2L = nums2[amtRemaining-1]
            if amtRemaining == len(nums2):
                val2R = math.inf
            else:
                val2R = nums2[amtRemaining]

            if valR < val2L:
                l = mid + 1
            elif valL > val2R:
                r = mid - 1
            else:
                break
        if (len(nums1) + len(nums2)) % 2 == 0:
            return (max(valL, val2L) + min(valR, val2R)) / 2
        else:
            return max(val2L, valL)
        
        
            

            
            
        
