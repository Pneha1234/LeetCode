class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum_sum = nums[0]
        sum = 0
        for i in range(len(nums)):
            sum +=nums[i]
            if sum > maximum_sum:
                maximum_sum = sum
            if sum < 0:
                sum = 0
        return maximum_sum
        