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

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        temp = {}
        for i in range(len(nums)):
            if nums[i] in temp:
                if i - temp[nums[i]] <= k:
                    return True
                else:
                    temp[nums[i]] = i
            else:
                temp[nums[i]] = i
        return False

    def containsNearbyDuplicate_v2(self, nums, k):
        temp = {}
        for i, key in enumerate(nums):
            if key in temp and i - temp[key] <= k:
                return True
            temp[key] = i
        return False

    def generate(self, numRows):
        """
        给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        index = 2
        p = [1]
        result = [p]
        # if numRows == 1:
        #     return result
        while index <= numRows:
            index += 1
            p = [1] + [p[i] + p[i + 1] for i in range(len(p) - 1)] + [1]
            result.append(p)
        return result

    def generate_v2(self, numRows):
        result = [[1]]
        for i in range(1, numRows):
            result.append(list(map(lambda x, y: x + y, result[-1] + [0], [0] + result[-1])))
        return result[:numRows]

if __name__ == '__main__':
    solution = Solution()
    print(solution.generate_v2(4))
