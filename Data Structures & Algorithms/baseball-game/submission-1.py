class Solution:
    def calPoints(self, operations: List[str]) -> int:

        scores = []

        for op in operations:
            if op == "+":
                v1 = scores.pop()
                v2 = scores.pop()
                scores.extend([v2, v1, v1 + v2])
            elif op == "D":
                v1 = scores.pop()
                scores.extend([v1, v1*2])
            elif op == "C":
                scores.pop()
            else:
                scores.append(int(op))
        
        return sum(scores)

        