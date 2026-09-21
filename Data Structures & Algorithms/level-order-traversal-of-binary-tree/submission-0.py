# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #go through, add elements to a queue, go until queue is empty, add the siblings to the queue
        if not root:
            return []

        q = deque()
        q.append(root)
        res = []
        while q:
            secondQ = deque()
            temp = []
            while q:
                v = q.popleft()
                if v.left:
                    secondQ.append(v.left)
                if v.right:
                    secondQ.append(v.right)
                temp.append(v.val)
            res.append(temp)
            q = secondQ
            
        return res
            