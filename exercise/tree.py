# -*- coding: utf-8 -*-
# @Time    : 2018/7/24 下午7:43
# @Author  : zhouyajun

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None:
            return
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        t1.value += t2.value
        t1.right = self.mergeTrees(t1.right, t2.right)
        t1.left = self.mergeTrees(t1.left, t2.left)
        return t1

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        # left_length = 1 + self.maxDepth(root.left)
        # right_length = 1 + self.maxDepth(root.right)
        # return max(left_length, right_length)
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def invertTree(self, root):
        """
        输入：

                 4
               /   \
              2     7
             / \   / \
            1   3 6   9
        输出：

                 4
               /   \
              7     2
             / \   / \
            9   6 3   1
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    def averageOfLevels(self, root):
        """
        给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.
        :type root: TreeNode
        :rtype: List[float]
        """
        result = []
        if root is None:
            return 0
        result.append((root.left.val + root.right.val) / 2)
        self.averageOfLevels(root.left)


if __name__ == '__main__':
    t1 = TreeNode(3)
    t2 = TreeNode(4)
    t1.right = t2
    solution = Solution()
    print(solution.averageOfLevels(t1))

