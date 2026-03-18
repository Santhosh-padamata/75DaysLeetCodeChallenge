class Solution(object):
    def countSubmatrices(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        dp = [[0] * cols for _ in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                # Standard 2D prefix sum formula
                current_sum = grid[r][c]
                
                if r > 0:
                    current_sum += dp[r-1][c]
                if c > 0:
                    current_sum += dp[r][c-1]
                if r > 0 and c > 0:
                    current_sum -= dp[r-1][c-1]
                
                dp[r][c] = current_sum
            
                if dp[r][c] <= k:
                    count += 1
                else:
                
                    break 
                    
        return count
