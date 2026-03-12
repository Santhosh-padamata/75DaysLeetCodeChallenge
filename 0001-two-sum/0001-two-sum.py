class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a={}
        for i in range(len(nums)):
            if target - nums[i] in a:
                return [a[target-nums[i]],i]
            a[nums[i]]=i