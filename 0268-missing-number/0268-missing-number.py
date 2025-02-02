class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_nums = 0
        n = len(nums)
        sum_natural_numbers = (n*(n+1))/2
        print(sum_natural_numbers)
        for i in range(len(nums)):
            sum_nums +=nums[i]
        return int(sum_natural_numbers-sum_nums)

        