class Solution:
    #solution1: two pass algorithm
    #time: O(N), space: O(1)
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow, fast = head, head
        while n > 0:
            fast = fast.next
            n -= 1
        
        if not fast:
            return slow.next
        
        while fast.next:
            slow, fast = slow.next, fast.next
        
        slow.next = slow.next.next
        
        return head