class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        final_result = [[1]]
        for i in range(1, numRows):
            final_result.append(self.getRow(i))
        return final_result
    
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]
        ans = 1
        rowIndex=rowIndex+1
        for i in range(1,rowIndex):
            ans = (ans*((rowIndex-i)/i))
            result.append(round(ans))
        return result

    


        