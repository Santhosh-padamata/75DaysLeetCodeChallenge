class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        max_len=len(nums)
        count=0
        for i in nums:
            if i==val:
                count=count+1
        for j in range(count):
            nums.remove(val)

        return max_len-count
        