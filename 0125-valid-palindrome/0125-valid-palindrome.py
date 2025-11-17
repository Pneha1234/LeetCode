class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(ch.lower() for ch in s if ch.isalnum())
        return self.check(clean, 0, len(clean) - 1)

    def check(self, s, i, j):
        # base case
        if i >= j:
            return True
        
        # if mismatch → not a palindrome
        if s[i] != s[j]:
            return False
        
        # recursive call
        return self.check(s, i + 1, j - 1)
