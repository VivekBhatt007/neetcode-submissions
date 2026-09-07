# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
        
        curr = s
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        m_sum = 0
        while prev:
            m_sum = max(m_sum, head.val + prev.val)
            head = head.next
            prev = prev.next
        return m_sum
        