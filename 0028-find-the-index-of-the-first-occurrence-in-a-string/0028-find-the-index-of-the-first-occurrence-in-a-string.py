class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        text_length = len(haystack)
        pattern_length = len(needle)

        # Edge case: If pattern is longer than text, it can't be found
        if pattern_length > text_length:
            return -1

        # Iterate through the text, checking substrings of length `pattern_length`
        for i in range(text_length - pattern_length + 1):
            if haystack[i : i + pattern_length] == needle:
                return i  # Return the first occurrence index

        return -1  # If not found
