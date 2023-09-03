class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # dp, bottom up
        n = len(matrix)
        
        if (n == 1):
            return matrix[0][0]
        
        self.sol = [[0] * n for i in range(n)]
        
        # space opt available
        for i in range(n):
            self.sol[-1][i] = matrix[-1][i]
            
        for i in range(n-2, -1, -1):
            for j in range(n):
                if (j == 0):
                    self.sol[i][j] = matrix[i][j] + min(self.sol[i+1][j], self.sol[i+1][j+1])
                    
                elif (j == n-1):
                    self.sol[i][j] = matrix[i][j] + min(self.sol[i+1][j], self.sol[i+1][j-1])
                    
                else:
                    self.sol[i][j] = matrix[i][j] + min(self.sol[i+1][j], self.sol[i+1][j-1], self.sol[i+1][j+1])
                    
                    
        return min(self.sol[0])