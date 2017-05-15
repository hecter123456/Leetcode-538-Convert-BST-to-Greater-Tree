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
        TreeSolution().checkAns(root,row)
    def testBinaryTree(self):
        row = [1,3,2,5,3,None,9]
        root = TreeSolution().AddBinaryTreeNode(row)
        TreeSolution().checkAns(root,row)
    def testNodeValEqualZeroTree(self):
        row = [2,0,3,-4,1]
        root = TreeSolution().AddBinaryTreeNode(row)
        TreeSolution().checkAns(root,row)
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
                if row[i] is not None:
                    node.left = TreeNode(row[i])
                i = i+1
            if i < len(row):
                if row[i] is not None:
                    node.right = TreeNode(row[i])
                i = i+1
            queue += filter(None, (node.left,node.right))
        return self.root
    def checkAns(self,root,ans):
        if not root:
            return
        ansqueue = [root]
        i = 0
        for node in ansqueue:
            if i < len(ans):
                if node is None:
                    unitest().assertEqual(node,ans[i])
                else:
                    unitest().assertEqual(node.val,ans[i])
                i += 1
            if node:
                ansqueue += (node.left,node.right)

if __name__ == '__main__':
    unittest.main()
