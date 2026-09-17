class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s) < len(t):
            return ""

        l,r = 0, 0
        hashTableT = {}
        hashTableS = {}

        for c in t:
            hashTableT[c] = hashTableT.get(c, 0) + 1

        matches, matchesNeeded = 0, len(hashTableT)
        minLength = math.inf
        minSubstring = ""
        while r < len(s):
            c = s[r]
            hashTableS[c] = hashTableS.get(c, 0) + 1
            if hashTableS[c] == hashTableT.get(c, 0):
                matches += 1
            print(matches)
            while matches == matchesNeeded:
                if minLength > r - l + 1:
                    minLength = r - l + 1
                    minSubstring = s[l:r+1]

                hashTableS[s[l]] = hashTableS.get(s[l], 0) - 1
                if hashTableS[s[l]] == hashTableT.get(s[l], 0) - 1:
                    matches -= 1
                l += 1
            r += 1
        
        return minSubstring
            
            




        