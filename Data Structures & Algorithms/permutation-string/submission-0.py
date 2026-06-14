class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq = {}
        for char in s1:
            freq[ord(char)] = freq.get(ord(char), 0) +  1
        #for each substring, count out the frequency chart, and compare
        #the substring would have to be len(s1) long

        l = 0
        r = len(s1)-1
        freqs2 = {}
        for i in range(len(s1)):
            freqs2[ord(s2[i])] = freqs2.get(ord(s2[i]), 0) + 1

        l = 0
        r = len(s1)-1
        while r < len(s2):
            print(freqs2)
            if freq == freqs2:
                return True
            else:
                freqs2[ord(s2[l])] = freqs2.get(ord(s2[l]), 0) -  1
                if freqs2[ord(s2[l])] == 0:
                    freqs2.pop(ord(s2[l]))
                l += 1
                r += 1
                if r < len(s2):
                    freqs2[ord(s2[r])] = freqs2.get(ord(s2[r]), 0) + 1
                
        return False

