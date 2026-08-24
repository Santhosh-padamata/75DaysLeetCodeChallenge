class Solution(object):

    def longestCommonPrefix(self, strs):
        prefix = ""

        minimum_str = min(strs, key=len)
        min_str_len = len(minimum_str)
        len_of_list = len(strs)

        for i in range(min_str_len):
            count = 0

            for j in strs:
                if j[i] == minimum_str[i]:
                    count = count + 1

            if count == len_of_list:
                prefix = prefix + minimum_str[i]
            else:
                break

        return prefix