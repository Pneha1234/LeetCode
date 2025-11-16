#User function Template for python3

class Solution:

    def printGfg(self, n):
        if n == 0:
            return
        print("GFG", end =" ")
        self.printGfg(n -1)
        