class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq = [0 for i in range(26)]
        for char in s1:
            freq[ord(char) - ord('a')] +=  1
        #for each substring, count out the frequency chart, and compare
        #the substring would have to be len(s1) long

        l = 0
        r = len(s1)-1
        freqs2 = [0 for i in range(26)]
        for i in range(len(s1)):
            freqs2[ord(s2[i]) - ord('a')] += 1

        l = 0
        r = len(s1)-1
        while r < len(s2):
            if freq == freqs2:
                return True
            else:
                freqs2[ord(s2[l]) - ord('a')] -=  1
                l += 1
                r += 1
                if r < len(s2):
                    freqs2[ord(s2[r]) - ord('a')] += 1
                
        return False

