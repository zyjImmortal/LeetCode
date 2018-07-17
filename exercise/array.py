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

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # temp = list(filter(lambda x: x != 0, nums1))
        nums_temp = []
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                nums_temp.append(nums1[i])
                i += 1
            else:
                nums_temp.append(nums2[j])
                j += 1
        nums_temp += nums1[i:]
        nums_temp += nums2[j:]
        return nums_temp


if __name__ == '__main__':
    solution = Solution()
    print(solution.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
