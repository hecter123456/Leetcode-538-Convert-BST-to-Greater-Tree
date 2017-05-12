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
        ans = [18,20,13]
        ansqueue = [root]
        i = 0
        for node in ansqueue:
            if i < len(ans):
                self.assertEqual(root.val,ans[i])
                i += 1
            ansqueue += (node.left,node.right)
    def testNegativeNode(self):
        row = [2,0,3,-4,1]
        tree = TreeSolution.TreeSolution()
        root = tree.AddBinaryTreeNode(row)
        Solution().convertBST(root)
        ans = [5,6,3,2,6]
        ansqueue = [root]
        i = 0
        for node in ansqueue:
            if i < len(ans):
                self.assertEqual(root.val,ans[i])
                i += 1
            ansqueue += (node.left,node.right)

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
