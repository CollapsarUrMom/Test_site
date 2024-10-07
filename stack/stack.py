from collections import deque 




class Solution:
    def isValid(self, s: str) -> bool:

        my_stack = deque()

        pairs = {'(' : ')',
                '[' : ']',
                '{' : '}'}
        

        for brasket in s:
            if brasket in pairs:
                my_stack.append(brasket)
            elif not my_stack:
                return False
            elif brasket != pairs[my_stack.pop()]:
                return False
        return len(my_stack) == 0



stack = Solution()

s = '()'
print(stack.isValid(s))
s = "()[]{}"
print(stack.isValid(s))
s = "(]"
print(stack.isValid(s))
s = "([])"
print(stack.isValid(s))
s = ']'
print(stack.isValid(s))