class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        element = -1
        for i in range(len(nums)):
            if cnt == 0:
                cnt = 1
                element = nums[i]
            elif element == nums[i]:
                cnt +=1
            else:
                cnt -=1
        counter = 0
        for i in range(len(nums)):
            if nums[i] == element:
                counter +=1
        if(counter > int(len(nums))/2):
            return element
        else:
            return -1




        