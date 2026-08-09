# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        #maybe something like if height diff by more than one, return -1
        #else, return 
        isBalanced = True
        
        def dfs(root):

            if not root:
                return 0
            nonlocal isBalanced

            maxL = dfs(root.left)
            maxR = dfs(root.right)

            if abs(maxL - maxR) > 1:
                isBalanced = False
            
            return 1 + max(maxL, maxR)
        
        dfs(root)
        return isBalanced
            
            