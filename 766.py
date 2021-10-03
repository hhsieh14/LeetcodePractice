class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if j - 1 >= 0 :
                    if matrix[i][j] != matrix[i - 1][j - 1]:
                        return False
        return True
