# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def levelOrder(root) -> List[List[int]]:
            ans = []
            q = []
            nq = []

            subans = []

            if root != None:
                q.append(root)

            while q:
                for parent in q:
                    if parent != None:
                        subans.append(parent.val)
                    else:
                        subans.append(None)
                    if parent != None and parent.left == None:
                        nq.append(None)
                    elif parent != None:
                        nq.append(parent.left)
                    if parent != None and parent.right == None:
                        nq.append(None)
                    elif parent != None:
                        nq.append(parent.right)
                q = nq
                nq = []
                ans.append(subans)
                subans = []

            return ans
        
        arr1 = levelOrder(p)
        arr2 = levelOrder(q)
        print(arr1,"\n",arr2)
        if arr1 != arr2:
            return False
        return True
        