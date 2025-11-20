class Solution:
    def insertSorted(self, st, val):
        # base case
        if not st or st[-1] <= val:
            st.append(val)
            return
        
        # otherwise remove top and insert val deeper
        temp = st.pop()
        self.insertSorted(st, val)
        st.append(temp)
        
    def sortStack(self, st):
        if not st:
            return
        
        top = st.pop()
        
        # sort remaining stack
        self.sortStack(st)
        
        # insert the popped element in sorted position
        self.insertSorted(st, top)

