import math
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]
        ans = 1
        rowIndex=rowIndex+1
        for i in range(1,rowIndex):
            print('ans:', ans)
            print('rowIndex:', rowIndex)
            print('i', i)
            ans = (ans*((rowIndex-i)/i))
            print('ans', ans)
            result.append(round(ans))
        return result



        