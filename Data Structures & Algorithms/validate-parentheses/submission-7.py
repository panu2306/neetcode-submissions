class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check_brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s: 
            if c == '[' or c == '{' or c == '(': 
                stack.append(c)
            elif stack and stack[-1] == check_brackets[c]: 
                stack.pop()
            else:
                return False
        return False if stack else True
        
        