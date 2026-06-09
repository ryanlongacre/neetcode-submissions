class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        leftBound = 0
        longestSub = 0
        lastApp = {}
        
        for i in range(len(s)):
            if s[i] in lastApp:
                leftBound = max(lastApp[s[i]] + 1, leftBound)
            lastApp[s[i]] = i
    
            longestSub = max(i + 1 - leftBound, longestSub)
        
        return longestSub

        

        