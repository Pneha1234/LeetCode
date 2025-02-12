class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1 = 0
        element1 = -1
        cnt2 = 0
        element2 = -1
        for i in range(len(nums)):
            if cnt1 == 0 and nums[i] != element2:
                cnt1 = 1
                element1 = nums[i]
            elif cnt2 == 0 and nums[i] != element1:
                cnt2 = 1
                element2 = nums[i]
            elif element1 == nums[i]:
                cnt1 += 1
            elif element2 == nums[i]:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        counter1 = 0
        counter2 = 0
        result = []
        for i in range(len(nums)):
            if nums[i] == element1:
                counter1 += 1
            elif nums[i] == element2:
                counter2 += 1

        for i in range(len(nums)):
            if counter1 > int(len(nums)) / 3 and element1 not in result:
                result.append(element1)
            elif counter2 > int(len(nums)) / 3 and element2 not in result:
                result.append(element2)

        return result