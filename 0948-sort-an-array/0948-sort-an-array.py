class Solution:
    def merge(self, nums, low, mid, high):
        tmp_list = []
        # [low.....mid] [mid+1....high]
        left = low
        right = mid+1
        while(left <= mid and right <= high):
            if nums[left] <= nums[right]:
                tmp_list.append(nums[left])
                left +=1
            else:
                tmp_list.append(nums[right])
                right +=1
        while(left <=mid):
            tmp_list.append(nums[left])
            left +=1
        while(right <= high):
            tmp_list.append(nums[right])
            right +=1
        nums[low:high+1] = tmp_list 


    def mergeSort(self, nums,low, high):
        if low >= high:
            return nums
        mid = (low + high)//2
        self.mergeSort(nums,low, mid)
        self.mergeSort(nums, mid+1, high)
        self.merge(nums, low, mid, high)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums)-1)
        return nums
        