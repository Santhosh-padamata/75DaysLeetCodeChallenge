class Solution(object):
    def getBiggestThree(self, grid):
        m = len(grid)
        n = len(grid[0])
        s = set()

        for i in range(m):
            for j in range(n):

                # single cell rhombus
                s.add(grid[i][j])

                k = 1
                while (i-k >= 0 and i+k < m and j-k >= 0 and j+k < n):

                    total = 0

                    # four edges
                    for d in range(k):
                        total += grid[i-k+d][j+d]      # top-right
                        total += grid[i+d][j+k-d]      # right-bottom
                        total += grid[i+k-d][j-d]      # bottom-left
                        total += grid[i-d][j-k+d]      # left-top

                    s.add(total)
                    k += 1

        ans = sorted(s, reverse=True)
        return ans[:3]