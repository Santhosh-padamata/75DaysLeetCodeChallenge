class Solution(object):
    def minAbsDiff(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        
        # Initialize the result matrix with correct dimensions
        res_m, res_n = m - k + 1, n - k + 1
        ans = [[0] * res_n for _ in range(res_m)]
        
        for i in range(res_m):
            for j in range(res_n):
                # 1. Extract all elements in the current k x k submatrix
                submatrix_elements = []
                for r in range(i, i + k):
                    for c in range(j, j + k):
                        submatrix_elements.append(grid[r][c])
                
                # 2. Get unique values and sort them
                unique_vals = sorted(list(set(submatrix_elements)))
                
                # 3. Calculate minimum absolute difference
                if len(unique_vals) < 2:
                    ans[i][j] = 0
                else:
                    min_diff = float('inf')
                    for idx in range(len(unique_vals) - 1):
                        diff = unique_vals[idx+1] - unique_vals[idx]
                        if diff < min_diff:
                            min_diff = diff
                    ans[i][j] = min_diff
                    
        return ans
