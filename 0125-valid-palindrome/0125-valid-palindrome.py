class Solution(object):
    def isPalindrome(self, s):
        filtered_chars = [char.lower() for char in s if char.isalnum()]
        return filtered_chars == filtered_chars[::-1]
