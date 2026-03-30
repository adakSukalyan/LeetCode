# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen=set()
        p=head
        while p!=None:
            p=p.next
            if p not in seen:
                seen.add(p)
            else:
                return True
        else:
            return False