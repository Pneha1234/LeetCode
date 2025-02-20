class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}  # Closing bracket to opening bracket mapping
    
        for char in s:
            if char in mapping:  # If it's a closing bracket
                top_element = stack.pop() if stack else '#'  # Pop from stack or use '#' as a dummy value
                if mapping[char] != top_element:
                    return False  # Mismatch found
            else:
                stack.append(char)  # Push opening bracket onto the stack
        
        return not stack  # If stack is empty, it's valid; otherwise, it's not
            