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
