class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow_pointer = nums[0]
        fast_pointer = nums[0]
        while True:
            slow_pointer = nums[slow_pointer]
            fast_pointer = nums[nums[fast_pointer]]
            if slow_pointer == fast_pointer:
                break

        # Phase 2: Find entry point of cycle (duplicate number)
        fast_pointer = nums[0]  # Reset fast pointer
        while slow_pointer != fast_pointer:
            slow_pointer = nums[slow_pointer]
            fast_pointer = nums[fast_pointer]

        return slow_pointer