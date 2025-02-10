class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1.0
        nn = abs(n)  # Take absolute value of n
        
        while nn:
            if nn % 2 == 1:  # If nn is odd, multiply ans by x
                ans *= x
                nn -= 1
            else:
                x *= x  # Square the base
                nn //= 2  # Integer division
        
        if n < 0:  # If n is negative, take reciprocal
            ans = 1 / ans
        
        return ans
