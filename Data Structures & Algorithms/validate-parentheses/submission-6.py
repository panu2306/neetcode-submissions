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
            elif stack and c in check_brackets: 
                if stack[-1] == check_brackets[c]: 
                    stack.pop()
                else:
                    return False
            else:
                return False
        if stack: 
            return False
        else: 
            return True
        
        