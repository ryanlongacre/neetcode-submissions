class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #key: count array, value: list of anagrams
        hashMap = {}
        for word in strs:
            count = [0] * 26
            for char in word: 
                count[ord(char)-97] += 1
            if tuple(count) in hashMap:
                hashMap[tuple(count)].append(word)
            else:
                hashMap[tuple(count)] = [word]
        finalList = []
        for anagramList in hashMap:
            finalList.append(hashMap[anagramList])
        return finalList