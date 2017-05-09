import unittest
import TreeSolution

class unitest(unittest.TestCase):
    def testNone(self):
        row = []
        tree = TreeSolution.TreeSolution()
        root = tree.AddBinaryTreeNode(row)
        self.assertEqual(Solution().convertBST(root),[]);

class Solution(object):
    def convertBST(self, root):
        if not root:
            return []

if __name__ == '__main__':
    unittest.main()
