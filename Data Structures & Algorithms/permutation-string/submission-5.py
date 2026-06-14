class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq = [0 for i in range(26)]
        freqs2 = [0 for i in range(26)]
        #for each substring, count out the frequency chart, and compare
        #the substring would have to be len(s1) long

        l = 0
        freqs2 = [0 for i in range(26)]
        for i in range(len(s1)):
            freqs2[ord(s2[i]) - ord('a')] += 1
            freq[ord(s1[i]) - ord('a')] +=  1

        matches = 0
        for i in range(26):
            matches += (1 if freq[i] == freqs2[i] else 0)


        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            index = ord(s2[r]) - ord('a')
            freqs2[index] += 1
            if freq[index] == freqs2[index]:
                matches += 1
            elif freq[index] + 1 == freqs2[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord('a')
            freqs2[index] -= 1
            if freq[index] == freqs2[index]:
                matches += 1
            elif freq[index] - 1 == freqs2[index]:
                matches -= 1
            l += 1
            r += 1
                
                
        return matches == 26

