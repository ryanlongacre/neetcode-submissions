class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        leftBound = 0
        longestSub = 0
        lastApp = {}
        
        for i in range(len(s)):
            if s[i] in lastApp and lastApp[s[i]] >= leftBound:
                leftBound = lastApp[s[i]] + 1
                lastApp[s[i]] = i
            else:
                lastApp[s[i]] = i
    
            longestSub = max(i + 1 - leftBound, longestSub)
        
        return longestSub

        

        