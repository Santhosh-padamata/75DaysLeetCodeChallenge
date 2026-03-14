class Solution(object):
    def getHappyString(self, n, k):
        res = []

        def backtrace(s):
            if len(s) == n:
                res.append(s)
                return
            
            for ch in ['a','b','c']:
                if not s or s[-1] != ch:
                    backtrace(s + ch)

        backtrace("")

        if k > len(res):
            return ""
        return res[k-1]