# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #so it must be a local maximum on the path to that node, so just dfs while keeping track of the local maximum?
        #don't have to keep track of seen nodes, because its a tree so everything will only guaranteed to be seen once
        def dfs(root, localMax):
            if not root:
                return 0
            m = root.val >= localMax
            localMax = max(localMax, root.val)
            l = dfs(root.left, localMax)
            r = dfs(root.right, localMax)
            
            return m + l + r
        
        
        return dfs(root, -math.inf)

    
        