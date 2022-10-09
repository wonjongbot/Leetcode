# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper (root, p, q):
            if root == None:
                return None
            if(root.val > p.val and root.val > q.val):
                return helper(root.left, p, q)
            if(root.val < p.val and root.val < q.val):
                return helper(root.right, p, q)
            return root
        LCA = helper(root,p,q)
        print(LCA)
        return LCA