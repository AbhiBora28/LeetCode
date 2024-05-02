class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def reverseLinkedList(node):
            prev = None
            current = node
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev
        
       
        def findLength(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length
        
        if not head or not head.next:
            return True
        
        length = findLength(head)
        mid = length // 2
        
       
        slow = fast = head
        for _ in range(mid):
            fast = fast.next
        
    
        second_half = reverseLinkedList(fast)
        
       
        while second_half:
            if head.val != second_half.val:
                return False
            head = head.next
            second_half = second_half.next
        
        return True


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


