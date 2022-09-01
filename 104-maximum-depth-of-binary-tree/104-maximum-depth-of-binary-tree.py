# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        else:
            leftmax = self.maxDepth(root.left) + 1
            rightmax = self.maxDepth(root.right) + 1
            if leftmax > rightmax:
                return leftmax
            else:
                return rightmax
