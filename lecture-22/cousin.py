# Question: https://leetcode.com/problems/cousins-in-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        xx = self.findNode(root, x)
        yy = self.findNode(root, y)
        
        return ((self.level(root, xx, 0) == self.level(root, yy, 0))
               and (not self.isSibling(root, xx, yy)))
    

    def isSibling(self, node, x, y):
        if node == None:
            return False
        return ((node.left == x and node.right == y) or (node.left == y and node.right == x) or self.isSibling(node.left, x, y) or self.isSibling(node.right, x, y))
        
        
    def level(self, node, x, level):
        if node == None:
            return 0
        if node == x:
            return level
        l = self.level(node.left, x, level+1)
        if l != 0:
            return l
        return self.level(node.right, x, level+1)
    
    def findNode(self, node, x):
        if node == None:
            return None
        if node.val == x:
            return node
        n = self.findNode(node.left, x)
        if n != None:
            return n
        return self.findNode(node.right, x)