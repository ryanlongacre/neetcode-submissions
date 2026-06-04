class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            charList = [0] * 26
            for c in s:
                charList[ord(c) - ord('a')] += 1
            ans[tuple(charList)].append(s)
        
        return list(ans.values())