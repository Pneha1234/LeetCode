class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort in place
        ans = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:  # Avoid duplicate triplets
                continue
            
            j, k = i + 1, len(nums) - 1
            
            while j < k:
                sum_sorted_array = nums[i] + nums[j] + nums[k]
                
                if sum_sorted_array > 0:
                    k -= 1  # Move right pointer left
                elif sum_sorted_array < 0:
                    j += 1  # Move left pointer right
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    
                    # Skip duplicate values
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        
        return ans