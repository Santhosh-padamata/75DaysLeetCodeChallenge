class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n=int(''.join(map(str,digits)))
        n=n+1
        lst=[int(x) for x in str(n)]
        return lst

        