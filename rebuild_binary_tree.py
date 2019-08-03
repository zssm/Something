class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return None
        root = TreeNode(pre.pop(0))

        index = tin.index(root.val)
        root.left = self.reConstructBinaryTree(pre, tin[:index])
        root.right = self.reConstructBinaryTree(pre, tin[index + 1:])
        return root


a=[1,2,3,4,5,6,7]
b=[3,2,4,1,6,5,7]
test=Solution()
print(test.reConstructBinaryTree(a,b))
