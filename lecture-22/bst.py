from collections import deque

class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left, self.right = None, None

class BST:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root == None

    def insert(self, val):
        self.root = self.insertHelper(val, self.root)
    def insertHelper(self, value, node):
        if node == None:
            node = TreeNode(value)
            return node

        # left
        if node.value > value:
            node.left = self.insertHelper(value, node.left)
        if node.value < value:
            node.right = self.insertHelper(value, node.right)

        return node

    def display(self):
        self.displayHelper(self.root, "Root Node: ")
    def displayHelper(self, node, details):
        if node == None:
            return

        print(details, node.value)

        self.displayHelper(node.left, "Left child of " + str(node.value) + " : ")
        self.displayHelper(node.right, "Right child of " + str(node.value) + " : ")


    def populate(self, nums):
        for num in nums:
            self.insert(num)

    def populateWithSorted(self, nums):
        self.populateWithSortedHelper(nums, 0, len(nums))
    def populateWithSortedHelper(self, nums, start, end):
        if start >= end:
            return
        mid = (start + end) // 2
        self.insert(nums[mid])

        self.populateWithSortedHelper(nums, start, mid)
        self.populateWithSortedHelper(nums, mid+1, end)

    def height(self):
        return self.heightHelper(self.root)
    def heightHelper(self, node):
        if node == None:
            return 0
        return 1 + max(self.heightHelper(node.left), self.heightHelper(node.right))

    def balanced(self):
        left = self.heightHelper(self.root.left)
        right = self.heightHelper(self.root.right)
        return abs(left - right) <= 1

    # sum of all nodes
    def sum(self):
        return self.sumHelper(self.root)
    def sumHelper(self, node):
        if node == None:
            return 0
        return node.value + self.sumHelper(node.left) + self.sumHelper(node.right)

    def traversals(self):
        self.preOrder(self.root)
        self.inOrder(self.root)
        self.postOrder(self.root)

    def preOrder(self, node):
        if node == None:
            return

        print(node.value)
        self.preOrder(node.left)
        self.preOrder(node.right)

    def inOrder(self, node):
        if node == None:
            return

        self.inOrder(node.left)
        print(node.value)
        self.inOrder(node.right)

    def postOrder(self, node):
        if node == None:
            return

        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.value)

    def removeLeaves(self):
        self.removeLeavesHelper(self.root)
    def removeLeavesHelper(self, node):
        if node == None:
            return

        if node.left != None and node.left.left == None and node.left.right == None:
            node.left = None

        if node.right != None and node.right.left == None and node.right.right == None:
            node.right = None

        self.removeLeavesHelper(node.left)
        self.removeLeavesHelper(node.right)


    # DFS
    def pathSum(self, sum):
        return self.checkPath(self.root, sum)
    def checkPath(self, node, sum):
        # base condition
        if node == None:
            return False

        if node.value == sum and node.left == None and node.right == None:
            return True

        return self.checkPath(node.left, sum-node.value) or self.checkPath(node.right, sum-node.value)

    def allPathSum(self, sum):
        result = []
        self.findAllPaths(self.root, sum, [], result)
        return result

    def findAllPaths(self, node, sum, currentList, result):
        if node == None:
            return

        currentList.append(node.val)

        if node.value == sum and node.left == None and node.right == None:
            result.append(list(currentList))
        else:
            self.findAllPaths(node.left, sum-node.value, currentList, result)
            self.findAllPaths(node.right, sum-node.value, currentList, result)

        # backtrack
        # remove current node
        del currentList[-1]

    # https://leetcode.com/problems/sum-root-to-leaf-numbers/
    def pathNumbersSum(self):
        return self.findPathNumbersSum(self.root, 0)
    def findPathNumbersSum(self, node, prevLevelSum):
        if node == None:
            return 0

        currentSum = node.value + prevLevelSum * 10

        if node.left == None and node.right == None:
            return currentSum

        return self.findPathNumbersSum(node.left, currentSum) + self.findPathNumbersSum(node.right, currentSum)

    

if __name__ == '__main__':
    bst = BST()
    # bst.insert(15)
    # bst.insert(10)
    # bst.insert(30)
    # bst.insert(14)
    # bst.insert(25)
    # bst.populate([15, 10, 30, 14, 25])
    bst.populateWithSorted([1,2,3,4,5,6])
    # print(bst.height())
    # print(bst.sum())
    # bst.display()
    print(bst.pathSum(90))
