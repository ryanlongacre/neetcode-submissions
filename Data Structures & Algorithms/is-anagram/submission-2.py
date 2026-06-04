class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        lettersOfS = [0] * 26
        lettersOfT = [0] * 26
        for i in range(len(s)):
            lettersOfS[ord(s[i]) - ord('a')] += 1
            lettersOfT[ord(t[i]) - ord('a')] += 1
        return lettersOfS == lettersOfT
        