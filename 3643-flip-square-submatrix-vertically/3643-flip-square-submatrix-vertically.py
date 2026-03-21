class Solution(object):
    def reverseSubmatrix(self, grid, x, y, k):
        """
        :type grid: List[List[int]]
        :type x: int (starting row)
        :type y: int (starting column)
        :type k: int (size of submatrix)
        :rtype: List[List[int]]
        """
       
        for i in range(k // 2):
            row1 = x + i
            row2 = x + k - 1 - i
            
            # Swap the elements in the range [y, y + k - 1] between row1 and row2
            for j in range(y, y + k):
                grid[row1][j], grid[row2][j] = grid[row2][j], grid[row1][j]
                
        return grid
