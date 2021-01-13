# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        output = ListNode()
        carry = 0
        cur = output
        while l1 or l2:
            cur1 = l1.val if l1 else 0
            cur2 = l2.val if l2 else 0

            num = cur1 + cur2 + carry
            cur.next = ListNode(num % 10)
            cur = cur.next
            carry = num // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry == 1:
            cur.next = ListNode(1)
        return output.next
