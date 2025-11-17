class Solution:
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1

    def skipSpace(self, s, i, n):
        while i < n and s[i] == ' ':
            i += 1
        return i

    def findSign(self, s, i, n):
        sign = 1
        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            sign = 1
            i += 1
        return sign, i

    def skipLeadingZeros(self, s, i, n):
        while i < n and s[i] == '0':
            i += 1
        return i

    def parseDigits(self, s, i, n, value, sign):
        # Base case: stop on non-digit or end of string
        if i == n or not s[i].isdigit():
            return value

        digit = ord(s[i]) - ord('0')

        # Overflow check: POSITIVE
        if sign == 1:
            if value > self.INT_MAX // 10 or (value == self.INT_MAX // 10 and digit > self.INT_MAX % 10):
                return self.INT_MAX

        # Overflow check: NEGATIVE (compare to abs(INT_MIN) = 2147483648)
        else:
            limit = -(self.INT_MIN)  # 2147483648
            if value > limit // 10 or (value == limit // 10 and digit > limit % 10):
                return self.INT_MIN

        newValue = value * 10 + digit
        return self.parseDigits(s, i + 1, n, newValue, sign)

    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        # 1. Skip whitespace
        i = self.skipSpace(s, i, n)

        # 2. Sign
        sign, i = self.findSign(s, i, n)

        # 3. Skip leading zeros
        i = self.skipLeadingZeros(s, i, n)

        # 4. Must start with digit
        if i == n or not s[i].isdigit():
            return 0

        # 5. Recursively parse digits (returns magnitude or clamped INT_MIN/INT_MAX)
        value = self.parseDigits(s, i, n, 0, sign)

        # 6. If parseDigits returned a clamped sentinel for negative overflow,
        #    it returns INT_MIN (already negative), so handle that:
        if value == self.INT_MIN:
            return self.INT_MIN
        if value == self.INT_MAX:
            # Could be the true magnitude (needs sign applied) OR an overflow sentinel.
            # Apply sign then clamp below — do not return here unconditionally.
            pass

        # 7. Apply sign to magnitude
        value *= sign

        # 8. Final safety clamp
        if value < self.INT_MIN:
            return self.INT_MIN
        if value > self.INT_MAX:
            return self.INT_MAX

        return value
