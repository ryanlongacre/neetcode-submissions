class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        numstack = []
        
        for item in tokens:
            if item == '+':
                numstack.append(numstack.pop() + numstack.pop())
            elif item == '-':
                num1, num2 = numstack.pop(), numstack.pop()
                numstack.append(num2-num1)
            elif item == '*':
                numstack.append(numstack.pop() * numstack.pop())
            elif item == '/':
                num1, num2 = numstack.pop(), numstack.pop()
                numstack.append(int(float(num2) /  num1))
            else:
                numstack.append(int(item))
        return numstack[0]
        