class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i,j in enumerate(nums):
            if j>=target:
                return i
            elif (target > max(nums)):
                return len(nums)
        