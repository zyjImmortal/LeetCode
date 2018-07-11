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



if __name__ == '__main__':
    solution = Solution()
    print(solution.findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]))
