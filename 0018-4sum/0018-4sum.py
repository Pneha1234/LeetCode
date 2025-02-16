class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Sort in place
        ans = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:  # Avoid duplicate quadruplets
                continue
            for j in range(i + 1, len(nums)):  # j should start after i
                if j > i + 1 and nums[j] == nums[j - 1]:  # Avoid duplicate quadruplets
                    continue

                k, l = j + 1, len(nums) - 1
                
                while k < l:
                    sum_sorted_array = nums[i] + nums[j] + nums[k] + nums[l]
                    
                    if sum_sorted_array > target:
                        l -= 1  # Move right pointer left
                    elif sum_sorted_array < target:
                        k += 1  # Move left pointer right
                    else:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        
                        # Skip duplicate values for k
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        # Skip duplicate values for l
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
        
        return ans
        