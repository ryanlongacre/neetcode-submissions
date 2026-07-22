# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #max length of the right and left, distance is max(right) + max(right)
        #but how do i go about doing this, because i need the max depth of right and left
        #maybe just return the max depth of right or left, as that will be in the final distance calc
        #but the longest doesn't have to go through the root, so maybe propagate the max distance up
        #but would have to pass not only the max distance, but the max of right and left to see if a longer max could be made
        #but i can only return one
        #so, i make a new function, that keeps track of the current max, and replaces it if a new max is found while dfsing the tree

        res = 0

        def dfs(root):


            if not root:
                return 0
            nonlocal res
            
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)
            #res is the max distance found beneath that node, either through that node or not
            #through means its right + left, not means it is entirely below (alreayd foudn)

            #now we propagate up the max depth of the tree up until that point
            return 1 + max(left, right)
        
        dfs(root)
        return res
        
        
        


        