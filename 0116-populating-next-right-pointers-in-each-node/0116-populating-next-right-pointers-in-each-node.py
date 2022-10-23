"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
            ans = []
            q = []
            nq = []

            subans = []

            if root != None:
                q.append(root)

            while q:
                for parent in q:
                    subans.append(parent)
                    if parent.left != None:
                        nq.append(parent.left)
                    if parent.right != None:
                        nq.append(parent.right)
                q = nq
                nq = []
                ans.append(subans)
                subans = []

            return ans
        arr = levelOrder(root)
        
        for subarr in arr:
            for i in range(len(subarr)):
                if i < len(subarr)-1:
                    subarr[i].next = subarr[i+1]
        return root
            