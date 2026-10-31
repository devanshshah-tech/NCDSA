# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recurse(prev, curr):
            if curr is None:
                return prev
            new_next = curr.next
            curr.next = prev
            return recurse(curr, new_next)
        return recurse(None, head)