class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1
        n=len(nums)
        # try to find the break point
        # Iterate from second last to the start
        for i in range(n - 2, -1, -1):
            if(nums[i])<nums[i+1]:
                index = i
                print(index)
                break
        
        # if index remains -1 then just reverse the list:
        if(index == -1):
            print('---')
            nums.reverse()
            return nums
            
        
        # Step 3: Find the smallest number greater than nums[index] to the right of it
        for j in range(n - 1, index, -1):  # Iterate from the end to index+1
            if nums[j] > nums[index]:
                # Swap nums[index] and nums[j]
                nums[index], nums[j] = nums[j], nums[index]
                break
        
        nums[index+1:] = reversed(nums[index+1:])


        