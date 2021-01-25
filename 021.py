# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #solution1: iteration
    #time: O(m + n), space: O(1)
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        if l1.val > l2.val:
            l1, l2 = l2, l1
        cur1, cur2 = l1.next, l2
        curHead = l1
        
        while cur1 and cur2:
            if cur1.val > cur2.val:
                curHead.next, cur2 = cur2, cur2.next
            else:
                curHead.next, cur1 = cur1, cur1.next
            curHead = curHead.next
        
        if not cur1:
            curHead.next = cur2
        if not cur2:
            curHead.next = cur1
        
        return l1