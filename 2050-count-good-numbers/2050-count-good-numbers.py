class Solution:
    MOD = 10 **9 +7

    def power(self, x, n):
        if n == 0:
            return 1
        
        if n % 2 == 0:
            half = self.power((x * x) % self.MOD, n // 2)
            return half
        else:
            return (x * self.power(x, n - 1)) % self.MOD

    def countGoodNumbers(self, n: int) -> int:
        # digit string is from 0 to 9
        # E 0 E 0 E 0 E 0 E 0 ---> Even = 5 and odd = 4

        #task to return the number of good digits , where n is the length of good string
        evens = (n + 1) // 2
        odds = n // 2
        
        even_choices = self.power(5, evens)   # 5 choices at even positions
        odd_choices = self.power(4, odds)    # 4 choices at odd positions
        
        return (even_choices * odd_choices) % self.MOD

