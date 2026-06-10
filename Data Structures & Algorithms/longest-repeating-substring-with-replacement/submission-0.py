class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {}
        l = 0
        r = 0
        maxFrequency = 0
        res = 0
        while r < len(s):
            chars[s[r]] = 1 + chars.get(s[r], 0)
            maxFrequency = max(maxFrequency, chars[s[r]])

            while (r - l + 1) - maxFrequency > k:
                chars[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        
        return res


        