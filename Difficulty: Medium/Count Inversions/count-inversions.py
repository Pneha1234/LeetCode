class Solution:
    #User function Template for python3
    def merge(self, nums, low, mid, high):
        tmp_list = []
        left = low
        right = mid + 1
        cnt = 0

        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                tmp_list.append(nums[left])
                left += 1
            else:
                tmp_list.append(nums[right])
                cnt += (mid - left + 1)  # Counting inversions
                right += 1

        while left <= mid:
            tmp_list.append(nums[left])
            left += 1

        while right <= high:
            tmp_list.append(nums[right])
            right += 1

        nums[low:high+1] = tmp_list
        return cnt

    def mergeSort(self, nums, low, high):
        cnt = 0
        if low >= high:
            return cnt
        mid = (low + high) // 2
        cnt += self.mergeSort(nums, low, mid)
        cnt += self.mergeSort(nums, mid + 1, high)
        cnt += self.merge(nums, low, mid, high)
        return cnt 
        
    #Function to count inversions in the array.
    def inversionCount(self, arr):
        nums = arr[:] 
        n = len(nums)
        return self.mergeSort(nums, 0, n - 1)
        
        # Your Code Here
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a))
        print("~")

# } Driver Code Ends