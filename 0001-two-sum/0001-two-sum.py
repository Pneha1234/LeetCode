class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            rem_value = target - nums[i]
            if rem_value in hash_map:
                # If the complement exists, return the result sorted
                return sorted([hash_map[rem_value], i])
            hash_map[nums[i]] = i
            