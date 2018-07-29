# -*- coding: utf-8 -*-
# @Time    : 2018/4/4 下午2:02
# @Author  : zhouyajun

import math


class Solution:

    def twoSum(self, nums, target):
        """
        给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = {}
        for i, j in enumerate(nums):
            table[j] = i
        for i, j in enumerate(nums):
            gap = target - j
            if gap in table.keys() and i != table[gap]:
                return [i, table[gap]]

    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        for i in str(num):
            a = []
            a.append(int(a))
            if len(a) > 1:
                self.addDigits(sum(a))
            else:
                return a[0]

    def add_digits(self, num):
        temp_list = list(map(int, str(num)))
        if len(temp_list) == 1:
            return num
        else:
            return self.add_digits(sum(temp_list))

    def addStrings(self, num1, num2):
        """
        :param num1: str
        :param num2: str
        :return: str
        """
        index1, index2 = len(num1) - 1, len(num2) - 1
        add = 0
        result = ''
        while index1 >= 0 or index2 >= 0:
            t1 = int(num1[index1]) if index1 >= 0 else 0
            t2 = int(num2[index2]) if index2 >= 0 else 0
            temp = t1 + t2 + add
            result = str(temp % 10) + result
            add = temp // 10
            index1 -= 1
            index2 -= 1
        if add == 1:
            result = str(1) + result
        return result

    def arrangeCoinsV1(self, n):
        """
        :type n: int
        :rtype: int
        """
        cur, rem = 1, n - 1
        while rem >= cur + 1:
            cur += 1
            rem -= cur
        return 0 if n == 0 else cur

    def arrangeCoinsV2(self, n):
        """
        :type n: int
        :rtype: int
        """
        ord()
        return int(-1 + math.sqrt(1 + 8 * n)) // 2

    def repeat(self, nums):
        import collections



solution = Solution()
print(solution.arrangeCoinsV2(8))