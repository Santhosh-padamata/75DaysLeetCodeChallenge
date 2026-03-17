class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        max_area = 0
        
        for i in range(len(matrix)):
            
            # build heights of consecutive 1s
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1 and i > 0:
                    matrix[i][j] += matrix[i-1][j]
            
            # sort row in descending order
            row = sorted(matrix[i], reverse=True)
            
            # calculate possible areas
            for j in range(len(row)):
                area = row[j] * (j + 1)
                max_area = max(max_area, area)
        
        return max_area