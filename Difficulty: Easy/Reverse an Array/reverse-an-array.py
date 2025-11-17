class Solution:
    def reverseArray(self, arr, i= 0, j =None):
        if j is None:
            j = len(arr) - 1
        
        if i >= j:
            return arr
        arr[i], arr[j] = arr[j], arr[i]
        self.reverseArray(arr, i=i+1, j =j-1)
        
        
        
        