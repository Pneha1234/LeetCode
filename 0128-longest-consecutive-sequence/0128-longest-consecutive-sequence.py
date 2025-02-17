class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # length of array
        n = len(nums)
        if n <=0:
            return 0
        longest = 1
        cnt = 0
        # have all values in set
        st = set(nums)

        for i in st:
            # find the starting point for the subsequence
            if i-1 not in st:
                # Reset count for each new sequence
                cnt =1
                x = i
                while x+1 in st:
                    cnt +=1
                    x +=1
            longest = max(longest, cnt)
        return longest



        