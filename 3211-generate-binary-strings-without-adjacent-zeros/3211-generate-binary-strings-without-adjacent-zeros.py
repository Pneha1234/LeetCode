class Solution:
    def validStrings(self, n: int, s="", last="1") -> List[str]:
        if len(s) == n:
            return [s]

        result = []

        # Always allowed: add '1'
        result += self.validStrings(n, s + "1", "1")

        # Add '0' ONLY if previous is '1'
        if last == "1":
            result += self.validStrings(n, s + "0", "0")

        return result


        
        