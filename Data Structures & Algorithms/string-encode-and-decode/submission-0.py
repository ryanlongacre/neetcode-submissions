class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        encodedString = "".join(strs)
        encodedString = ")" + encodedString
        for i in range(len(strs)):
            encodedString = str(len(strs[len(strs)-i-1])) + "," + encodedString
        
        return encodedString


    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        i = 0
        count = s.find(")")+1
        finishedList = []
        while (s[i] != ")"):
            num = int(s[i:s.find(",", i)])
            finishedList.append(s[count:count+num])
            i = s.find(",", i) + 1
            count+=num
        return finishedList
