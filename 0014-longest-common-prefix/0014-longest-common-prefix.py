class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Start with the first string as the prefix
        prefix = strs[0]

        for string in strs[1:]:
            # Compare the prefix with each string and trim it down
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix