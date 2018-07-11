class Solution:
    def twoSum(self, nums, target):
        """
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