
print('==========================================================')


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


    def pop(self):
        del self.val[-1]


    def popleft(self):
        del self.val[0]


    def sizeof(self):
        len(self.val)


class Solution:
    def isPalindrome(self, head: list[ListNode]) -> bool:
        while head.sizeof():
            if head.pop() == head.popleft():
                continue
            else:
                return False
        return True







head = [1,2,2,1]

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)

palindrome = Solution()

print(palindrome.isPalindrome(head))