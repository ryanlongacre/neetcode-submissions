class Solution:
    def isValid(self, s: str) -> bool:


        stack = []

        close = {')' : '(', '}' : '{', ']' : '['}
        
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if stack.pop() != close[c]:
                    return False
            
            
        
        return len(stack) == 0
        