# -*- coding: utf-8 -*-
# @Time    : 2018/7/25 下午4:51
# @Author  : zhouyajun

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
