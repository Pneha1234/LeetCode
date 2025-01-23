class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Step 1: Initialize extra_row and extra_column
        extra_row = [0] * len(matrix)
        extra_column = [0] * len(matrix[0])

        # Step 2: Mark rows and columns
        for i in range(len(matrix)):  
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    extra_row[i] = -1
                    extra_column[j]= -1
        for i in range(len(extra_row)):
            if extra_row[i] == -1:
                # Set entire row to 0
                for j in range(len(matrix[0])):
                    print(matrix[i][j])
                    matrix[i][j] = 0
        print(matrix)

        for j in range(len(extra_column)):
            if extra_column[j] == -1:
                # set entire column to 0
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        print(matrix)

    