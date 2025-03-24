#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
'''
class ListNode:
    def __init__(self, value):
        self.data = value
        self.next = None  # Initialize next pointer as None
        
class Solution:
    def constructLL(self, arr):
        if not arr:  # Handle edge case where the array is empty
            return None

        head = ListNode(arr[0])  # Create the head node from the first element
        current = head  # Pointer to track the last node in the linked list

        for value in arr[1:]:  # Iterate through the remaining array elements
            current.next = ListNode(value)  # Create a new node and link it
            current = current.next  # Move the pointer to the new node

        return head  # Return the head of the constructed linked list

        # code here


#{ 
 # Driver Code Starts.
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        # n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.constructLL(arr)
        while res:
            print(res.data, end = ' ')
            res = res.next
        print()
        print("~")
# } Driver Code Ends