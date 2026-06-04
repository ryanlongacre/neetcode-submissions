class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = "".join([char for char in s if char.isalnum()])
        clean_text = clean_text.lower()
        i = 0
        j = len(clean_text) - 1
        while i < j:
            if clean_text[i] != clean_text[j]:
                return False
            i += 1
            j -= 1
        return True
        