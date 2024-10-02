from collections import deque 




class Solution:
    def isValid(self, data: str) -> bool:

        my_stack = deque()

        pairs = {'(' : ')',
                '[' : ']',
                '{' : '}'}
        

        for brasket in data:
            if brasket in pairs:
                my_stack.append(brasket)
            elif brasket != pairs[my_stack.popleft()]:
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