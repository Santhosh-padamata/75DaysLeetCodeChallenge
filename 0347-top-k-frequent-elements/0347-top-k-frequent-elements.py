from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        return [x for x, y in Counter(nums).most_common(k)]