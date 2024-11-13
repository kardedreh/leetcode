class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in map:
                top_el = stack.pop() if stack else '*' #placeholder if stack is empty
                if map[char] != top_el:
                    return False
            else:
                stack.append(char)
        return not stack
