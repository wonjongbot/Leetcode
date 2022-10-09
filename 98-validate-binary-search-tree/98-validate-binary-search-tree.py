# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, lower, upper):
            if root == None:
                return True
            if (root.val <= lower or root.val >= upper):
                return False
            leftans = helper(root.left, lower, root.val)
            rightans = helper(root.right, root.val, upper)
            return leftans and rightans
        ans = helper(root, -2**31 - 1, 2**31)
        return ans
        