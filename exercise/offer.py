# -*- coding: utf-8 -*-
# @Time    : 2018/7/25 下午4:51
# @Author  : zhouyajun


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def find(self, target, array):
        """
        题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
        请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
        :param target:
        :param array:
        :return:
        """
        rows = len(array)
        columns = len(array[0])
        i, j = 0, columns - 1
        while i < rows and j < 0:
            if array[i][j] > target:
                j -= 1
            elif array[i][j] < target:
                i += 1
            else:
                return True
        return False

    def replace(self, s):
        return s.replace(' ', '%20')

    def print_node(self, nodes):
        p = nodes
        while p is not None:
            print(p.elem, end=' ')
            if p.next is not None:
                print(',', end=' ')
            p = p.next
        print(' ')

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        思路：
            1、确定根节点
            2、确定子节点的前序遍历范围和中序遍历范围
        """
        if not inorder:
            return None
        root = preorder[0]
        index = inorder.index(root)  # 获取根节点再中序遍历结果的索引，也就可以确定根节点左子树总共有多少个节点
        root.left = self.buildTree(preorder[1:index + 1], inorder[:index])
        root.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        return root

    def fib(self):
        pass

    def returnNthFromEnd(self, head, n):
        """
        输入一个链表，输出该链表中倒数第k个结点。
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        result = []
        pre = head
        result.append(pre)
        while pre.next:
            result.append(pre.next)
            pre = pre.next
        return result[-n]

    def removeNthFromEnd(self, head, n):
        """
        给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """



if __name__ == '__main__':
    solution = Solution()
    print()
