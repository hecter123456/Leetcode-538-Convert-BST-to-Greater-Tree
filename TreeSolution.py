import unittest

class TreeNode(object):
    def __init__(self, x = None):
        self.val = x
        self.left = None
        self.right = None

class unitest(unittest.TestCase):
    def testNone(self):
        row = []
        self.assertEqual(TreeSolution().AddBinaryTreeNode(row),None)
    def testCompleteBinaryTree(self):
        row = [2,1,3,6,5,4,7]
        root = TreeSolution().AddBinaryTreeNode(row)
        self.assertEqual(root.val,2)
        self.assertEqual(root.left.val,1)
        self.assertEqual(root.right.val,3)
        self.assertEqual(root.left.left.val,6)
        self.assertEqual(root.left.right.val,5)
        self.assertEqual(root.right.left.val,4)
        self.assertEqual(root.right.right.val,7)
    def testBinaryTree(self):
        row = [1,3,2,5,3,None,9]
        root = TreeSolution().AddBinaryTreeNode(row)
        self.assertEqual(root.val,1)
        self.assertEqual(root.left.val,3)
        self.assertEqual(root.right.val,2)
        self.assertEqual(root.left.left.val,5)
        self.assertEqual(root.left.right.val,3)
        self.assertEqual(root.right.left,None)
        self.assertEqual(root.right.right.val,9)
class TreeSolution(object):
    def __init__(self):
        self.root = None
    def AddBinaryTreeNode(self,row):
        if not row:
            return None
        i = 0
        self.root = TreeNode(row[i])
        i = i+1
        queue = [self.root]
        for node in queue:
            if i < len(row):
                if row[i]:
                    node.left = TreeNode(row[i])
                i = i+1
            if i < len(row):
                if row[i]:
                    node.right = TreeNode(row[i])
                i = i+1
            queue += filter(None, (node.left,node.right))
        return self.root

if __name__ == '__main__':
    unittest.main()
