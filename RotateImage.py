#in-place changing
#rotation = transpose + reflect from left to right
#time: O(M), space: O(1)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reflect(matrix)
        return matrix
        
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(int(n/2)):
                matrix[i][j], matrix[i][-(j+1)] = matrix[i][-(j+1)], matrix[i][j]
                
# if the problem wants to fix the diagonal elements, 
# only switch index not on the diagonal
# condition of diagonal elements: a. i+j == len(matrix)-1 b. i == j
class Solution_fixed_diagonal:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reflect(matrix)
        return matrix
        
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                if i+j != n-1:#differnce
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(int(n/2)):
                if i != j and i+j != n-1:#difference
                    matrix[i][j], matrix[i][-(j+1)] = matrix[i][-(j+1)], matrix[i][j]
