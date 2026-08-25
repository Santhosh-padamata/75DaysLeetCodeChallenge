class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_num=max(nums)
        for i in range(1,max_num*2):
            if ((i*k) not in nums):
                return i*k