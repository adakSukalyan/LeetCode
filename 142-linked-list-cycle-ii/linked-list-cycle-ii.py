# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen=set()
        p=head
        while p!=None:
            if p in seen:
                return p
            seen.add(p)
            p=p.next    
        return None