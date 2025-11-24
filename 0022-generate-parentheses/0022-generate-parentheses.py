class Solution:
    def generateParenthesis(self, n: int, s="",open=0, close=0) -> List[str]:
        if open == n and close == n:
            return [s]
        
        result= []
        # Add '(' if we still have more to use
        if open < n:
            result += self.generateParenthesis(n, s + '(', open +1, close)

         # Add ')' only if valid
        if close < open:
            result += self.generateParenthesis(n, s + ')', open, close +1)
        return result

        