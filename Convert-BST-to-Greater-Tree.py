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
        root = Solution().convertBST(root)
        ans = [18,20,13]
        tree.checkAns(root,ans)
    def testThirdLevelBST(self):
        row = [2,0,3,-4,1]
        tree = TreeSolution.TreeSolution()
        root = tree.AddBinaryTreeNode(row)
        root = Solution().convertBST(root)
        ans = [5,6,3,2,6]
        tree.checkAns(root,ans)
    def testRightChildrenNodeBST(self):
        row = [1,0,4,-2,None,3]
        tree = TreeSolution.TreeSolution()
        root = tree.AddBinaryTreeNode(row)
        root = Solution().convertBST(root)
        ans = [8,8,4,6,None,7]
        tree.checkAns(root,ans)

class Solution(object):
    def GreaterTree(self,root,num):
        if not root:
            return num
        rightVal = self.GreaterTree(root.right,num)
        root.val += rightVal
        leftVal = self.GreaterTree(root.left,root.val)
        return leftVal
    def convertBST(self, root):
        if not root:
            return []
        self.GreaterTree(root,0)
        return root
if __name__ == '__main__':
    unittest.main()
