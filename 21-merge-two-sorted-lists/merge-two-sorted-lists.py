# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1:
            p=list1
        else:
            return list2
        if list2:
            q=list2
        else:
            return list1
        head=ListNode(-1)
        r=head
        while p and q:
            if p.val <= q.val:
                r.next=p
                p=p.next
            elif p.val>=q.val:
                r.next=q
                q=q.next
            r=r.next
            if p:
                r.next=p
            else:
                r.next=q
        return head.next