#User function Template for python3

class Solution:
    def printNos(self, n):
        if n == 0:
            return
        print(n , end =" ")
        n =n-1
        self.printNos(n)