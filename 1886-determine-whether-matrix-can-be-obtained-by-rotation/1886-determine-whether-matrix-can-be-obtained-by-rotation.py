class Solution(object):
    def findRotation(self, mat, target):
        for _ in range(4):
            if mat == target:
                return True
            mat = self.rotate(mat)    
        return False

    def rotate(self, matrix):
       
        n = len(matrix)
        new_mat = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new_mat[j][n - 1 - i] = matrix[i][j]
        return new_mat
