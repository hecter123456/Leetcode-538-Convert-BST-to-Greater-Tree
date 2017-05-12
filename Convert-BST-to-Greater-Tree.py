import unittest
import TreeSolution

class unitest(unittest.TestCase):
    def testNone(self):
        row = []
        tree = TreeSolution.TreeSolution()
        root = tree.AddBinaryTreeNode(row)
        self.assertEqual(Solution().convertBST(root),[])
    def testSecondLevelBST(self):
        row = [5,2,13]
        tree = TreeSolution.TreeSolution()
        root = tree.AddBinaryTreeNode(row)
        Solution().convertBST(root)
        self.assertEqual(root.val,18)
        self.assertEqual(root.left.val,20)
        self.assertEqual(root.right.val,13)

class Solution(object):
    def GreaterTree(self,root,num):
        if not root:
            return 0
        add = 0
        if root.right:
            add =  self.GreaterTree(root.right,0)
        root.val += (add+num)
        if root.left:
            self.GreaterTree(root.left,root.val)
        return root.val
    def convertBST(self, root):
        if not root:
            return []
        self.GreaterTree(root,0)
if __name__ == '__main__':
    unittest.main()
