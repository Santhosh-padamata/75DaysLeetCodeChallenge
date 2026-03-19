class Solution(object):
    def numberOfSubmatrices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
      
        cntX = [[0] * (cols + 1) for _ in range(rows + 1)]
        cntY = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        ans = 0
        
        for r in range(rows):
            for c in range(cols):
                
                valX = 1 if grid[r][c] == 'X' else 0
                valY = 1 if grid[r][c] == 'Y' else 0
                
                cntX[r + 1][c + 1] = valX + cntX[r][c + 1] + cntX[r + 1][c] - cntX[r][c]
                cntY[r + 1][c + 1] = valY + cntY[r][c + 1] + cntY[r + 1][c] - cntY[r][c]
                
                if cntX[r + 1][c + 1] > 0 and cntX[r + 1][c + 1] == cntY[r + 1][c + 1]:
                    ans += 1
                    
        return ans
