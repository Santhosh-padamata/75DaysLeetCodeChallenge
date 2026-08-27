class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        e=set(nums)
        f=list(e)
        count1=0
        for i in f:
            a=nums.count(i)
            if (a>count1):
                count1=a
                s=f.index(i)
        return f[s]

        