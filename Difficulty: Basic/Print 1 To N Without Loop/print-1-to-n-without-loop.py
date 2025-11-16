class Solution:    
    def printNos(self,n, cnt=1):
        if cnt > n:
            return
        print(cnt , end=" ")
        cnt= cnt +1
        self.printNos(n ,cnt)