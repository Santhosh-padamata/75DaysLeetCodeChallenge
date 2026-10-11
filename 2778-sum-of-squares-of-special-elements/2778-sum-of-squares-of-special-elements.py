class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count = 0

        for i in range(1, n + 1):
            if n % i == 0:
                count += nums[i - 1] * nums[i - 1]

        return count