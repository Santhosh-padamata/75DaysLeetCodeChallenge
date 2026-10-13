class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(key=lambda x: x * x)

        n = len(nums)
        result = 0

        for i in range(n):
            if i < n // 2:
                result -= nums[i] * nums[i]
            else:
                result += nums[i] * nums[i]

        return result