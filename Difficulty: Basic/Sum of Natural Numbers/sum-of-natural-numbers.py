class Solution:
    def findSum(self, n):
        if n <= 0:
            return 0
        return n + self.findSum(n-1)
        
