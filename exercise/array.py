# -*- coding: utf-8 -*-
# @Time    : 2018/7/11 下午3:13
# @Author  : zhouyajun

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        a = 0
        # for i in range(len(nums) // 2):
        #     if i == len(nums) - 1:
        #         break
        #     result.append(min(nums[a], nums[a + 1]))
        #     a += 2
        # return sum(result)
        n = len(nums)
        mid = n // 2
        return sum(map(min, zip(nums[:mid], nums[mid:n])))

    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        result = 0
        for i in s:
            for j in g:
                if i >= j:
                    result += 1
                    g.remove(j)
                    break
        return result

    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        pass

    def merge(self, nums1, nums2):
        """
        给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

        说明:
            初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
            你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # temp = list(filter(lambda x: x != 0, nums1))
        nums_temp = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums_temp.append(nums1[i])
                i += 1
            else:
                nums_temp.append(nums2[j])
                j += 1
        nums_temp += nums1[i:]
        nums_temp += nums2[j:]
        return nums_temp

    def sortList(self, seq):
        """归并排序nlogn时间复杂度，空间复杂度常数级"""
        if len(seq) <= 1:
            return seq
        mid = int(len(seq) / 2)
        left = self.sortList(seq[:mid])
        right = self.sortList(seq[mid:])
        return self.merge(left, right)


if __name__ == '__main__':
    solution = Solution()
    print(solution.sortList([-1, 4, 5, 2, 9, 1, 1, 1, 2, 3]))
