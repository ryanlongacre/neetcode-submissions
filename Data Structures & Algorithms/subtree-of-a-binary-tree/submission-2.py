# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False
        
        l = self.isSubtree(root.left, subRoot)
        r = self.isSubtree(root.right, subRoot)

        return self.isSame(root, subRoot) or l or r





    def isSame(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        l = self.isSame(p.left, q.left)
        r = self.isSame(p.right, q.right)

        return p.val == q.val and l and r
        