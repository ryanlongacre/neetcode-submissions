class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        boxes = defaultdict(set)
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                if val in cols[j]:
                    return False
                else:
                    cols[j].add(val)
                if val in rows[i]:
                    return False
                else:
                    rows[i].add(val)
                if val in boxes[tuple([i//3, j//3])]:
                    return False
                else:
                    boxes[tuple([i//3, j//3])].add(val)
        return True