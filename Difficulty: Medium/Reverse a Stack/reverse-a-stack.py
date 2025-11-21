class Solution:
    def insertAtBottom(self, st, item):
        if not st:
            st.append(item)
            return
        
        top = st.pop()
        self.insertAtBottom(st, item)
        st.append(top)

    def reverseStack(self, st):
        if not st:
            return
        
        top = st.pop()
        self.reverseStack(st)
        self.insertAtBottom(st, top)
