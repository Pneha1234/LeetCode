class Solution:
    def binstr(self, n, s="", last='0'):
        if len(s) == n:
            return [s]
        
        result = []

        # Always allowed to add 0
        result += self.binstr(n, s + '0', '0')

        # Add 1 only when last is 0
        # if last == '0':
        result += self.binstr(n, s + '1', '1')

        return result
