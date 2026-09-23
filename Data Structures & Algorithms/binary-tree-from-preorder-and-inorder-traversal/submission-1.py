# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #preorder is root -> left -> right
        #inorder is left -> root -> right

        idx = {val: i for i, val in enumerate(inorder)}

        self.pre_i = 0

        def build(lo, hi):
            if lo > hi:
                return None
            
            root_val = preorder[self.pre_i]
            self.pre_i += 1
            root = TreeNode(root_val)

            mid = idx[root_val]
            #the nature of the function makes both of these inclusive
            root.left = build(lo, mid-1)
            root.right = build(mid+1, hi)
            return root
        
        return build(0, len(inorder)-1)
