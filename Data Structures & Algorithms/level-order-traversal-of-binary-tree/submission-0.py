# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        result = []
        if not root:
            return result
        q.append(root)
        while q:
            l = len(q)
            temp = []
            for i in range(l):
                cur = q.popleft()
                temp.append(cur.val)
            
                if cur.left !=None:
                    q.append(cur.left)
                if cur.right != None:
                    q.append(cur.right)
            result.append(temp)
        return result