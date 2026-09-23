# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def valid(node, left, right):
            if not node:
                return True
            
            l = valid(node.left, left, node.val)
            r = valid(node.right, node.val, right)
            return node.val < right and node.val > left and l and r
        
        return valid(root, -math.inf, math.inf)