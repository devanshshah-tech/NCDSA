class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] == '{' or s[i] == '(' or s[i] == '[':
                stack.append(s[i])

            else:

                if len(stack) == 0:
                    return False 
                    
                char = stack.pop()

                if char == '(' and s[i] != ')':
                    return False
                if char == '[' and s[i] != ']':
                    return False
                if char == '{' and s[i] != '}':
                    return False

        return len(stack) == 0