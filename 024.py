# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # solution1
    # time: O(N), space: O(1)
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        p1, p2 = head, head.next
        head = p2

        while p2.next and p2.next.next:
            p3, p4 = p2.next, p2.next.next
            p1.next, p2.next = p4, p1
            p1, p2 = p3, p4
        if p2.next:
            p1.next, p2.next = p2.next, p1
        else:
            p1.next, p2.next = None, p1

        return head
