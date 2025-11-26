class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(i, current):
            # If we've considered all elements, record current subset
            if i == len(nums):
                result.append(current[:])
                return
            
            # 1. Include nums[i]
            backtrack(i + 1, current + [nums[i]])
            
            # 2. Exclude nums[i]
            backtrack(i + 1, current)

        backtrack(0, [])
        return result
