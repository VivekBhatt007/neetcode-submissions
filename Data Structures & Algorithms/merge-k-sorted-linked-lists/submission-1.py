# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:


        # if len(lists) == 0:
        #     return None

        # res = ListNode(0)
        # curr = res
        # minHeap = []

        # for l in lists:
        #     if l is not None:
        #         heapq.heappush(minHeap, NodeWrapper(l))
        
        # while minHeap:
        #     nWrape = heapq.heappop(minHeap)
        #     curr.next = nWrape.node
        #     curr = curr.next

        #     if nWrape.node.next:
        #         heapq.heappush(minHeap, NodeWrapper(nWrape.node.next))

        # return res.next


        def mergeLists(l1, l2) -> ListNode:
            dummy = curr = ListNode(0)

            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                    curr = curr.next
                else:
                    curr.next = l2
                    l2 = l2.next
                    curr = curr.next
            if l1:
                curr.next = l1
            else:
                curr.next = l2
            return dummy.next
        
        l = len(lists)
        if l == 0:
            return None
        elif l == 1 and len(list[0]) == 0:
            return None

        l -= 1
        while l:
            lists[0] = mergeLists(lists[0], lists[l])
            l -= 1
        return lists[0]