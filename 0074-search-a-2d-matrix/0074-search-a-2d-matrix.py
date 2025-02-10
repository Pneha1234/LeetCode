from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:  # Handle empty matrix cases
            return False
        
        n = len(matrix)
        m = len(matrix[0])
        low, high = 0, (n * m) - 1  
        
        while low <= high:
            mid = (low + high) // 2  # Integer division
            row = mid // m  #  row calculation
            column = mid % m  # column calculation
            
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return False
