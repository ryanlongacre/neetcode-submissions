class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        leftRow = 0
        rightRow = len(matrix) - 1
        while leftRow <= rightRow:
            midRow = leftRow + (rightRow - leftRow) // 2
            endRow = matrix[midRow][len(matrix[0])-1]
            if target == endRow:
                return True
            elif endRow > target:
                if target >= matrix[midRow][0]:
                    break
                else:
                    rightRow = midRow - 1
            else:
                leftRow = midRow + 1
        targetRow = matrix[midRow]
        left = 0
        right = len(targetRow) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target == targetRow[mid]:
                return True
            elif target < targetRow[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return False


        