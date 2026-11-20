class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s1, s2 = 0, 0
        res = ""

        while s1 < len(word1) and s2 < len(word2):
            res += word1[s1] + word2[s2]
            s1 += 1
            s2 += 1
        
        res += word1[s1:]
        res += word2[s2:]

        return res