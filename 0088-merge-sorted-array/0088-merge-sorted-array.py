class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left_pointer = m - 1 
        right_pointer = 0  
        while left_pointer >= 0 and right_pointer < n:
            print(nums1[left_pointer])
            print(nums2[right_pointer])
            if nums1[left_pointer] > nums2[right_pointer]:
                nums1[left_pointer], nums2[right_pointer] = nums2[right_pointer], nums1[left_pointer]
            print(nums1)
            print(nums2)
            left_pointer -= 1
            right_pointer += 1
        nums1[m:] = nums2 
        nums1.sort()
        