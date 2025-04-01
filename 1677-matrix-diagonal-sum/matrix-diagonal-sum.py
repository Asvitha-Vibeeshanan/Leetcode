class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if len(mat) - 1 == i+j or i == j:
                    sum = sum + mat[i][j]
        return sum