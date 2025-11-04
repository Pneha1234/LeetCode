class Solution:
    def insertionSort(self, arr):
        for i in range(len(arr)):
            j = i
            while(j>0 and arr[j-1] > arr[j]):
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -=1
        return arr
                