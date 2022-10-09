# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        parr = []
        qarr = []
        
        def inorder_helper(root, ans):
            if root == None:
                ans.append(None)
                return
            inorder_helper(root.left, ans)
            inorder_helper(root.right, ans)
            ans.append(root.val)
            
        inorder_helper(p, parr)
        inorder_helper(q, qarr)
        
        print(parr, "\n", qarr)
        
        if parr == qarr:
            return True
        else:
            return False