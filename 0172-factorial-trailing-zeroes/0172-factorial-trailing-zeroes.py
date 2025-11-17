class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        """ the idea is to find the remainder of 5, something like for 100,the solution will look like 100 // 5 = 20, so 20 + self.trailingZeroes(20)"""
        return n//5 + self.trailingZeroes(n//5)
        