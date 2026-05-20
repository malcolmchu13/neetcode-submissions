# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque()

        if root: 
            q.append(root)
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.val == subRoot.val: 
                    if self.isSametree(node, subRoot): 
                        return True        
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
        return False

    def isSametree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True 
        if not p or not q: return False 
        q1 = deque()
        q2 = deque() 
        
        if p and q: 
            q1.append(p)
            q2.append(q)
        
        while q1 and q2:
            for i in range(len(q1)): 
                nodep = q1.popleft()
                nodeq = q2.popleft()
                if nodep.val != nodeq.val: 
                    return False 
                if (nodep.left is None) != (nodeq.left is None):   
                    return False
                if (nodep.right is None) != (nodeq.right is None): 
                    return False
                if nodep.left:
                    q1.append(nodep.left)
                    q2.append(nodeq.left)
                if nodep.right:
                    q1.append(nodep.right)
                    q2.append(nodeq.right)
        return True

