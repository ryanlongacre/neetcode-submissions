# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #only want the last element of each level
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []

        while q:
            qLen = len(q)

            for i in range(qLen):
                v = q.popleft()
                if i == qLen-1:
                    res.append(v.val)
                
                if v.left:
                    q.append(v.left)
                if v.right:
                    q.append(v.right)
        return res
        