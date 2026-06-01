class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for c in s:
            if(c in ['{', '(', '[']):
                stack.append(c)
            elif(stack and c == hashmap[stack[-1]]):
                stack.pop()
            else:
                return False
        return True if not stack else False
        
        