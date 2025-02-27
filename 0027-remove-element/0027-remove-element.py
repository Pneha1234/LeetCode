class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Pointer to track the position of non-val elements
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        return k
        