# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = []
        nq = []
        
        subans = []
        
        if root != None:
            q.append(root)
        
        while q:
            for parent in q:
                subans.append(parent.val)
                if parent.left != None:
                    nq.append(parent.left)
                if parent.right != None:
                    nq.append(parent.right)
            q = nq
            nq = []
            ans.append(subans)
            subans = []
                    
        return ans
        
        