class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a=str(x)
        y=a[::-1]
        if(y==a):
            return True
        else:
            return False

        