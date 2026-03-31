# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p=head
        q=head
        count=1
        while(p.next != None):
            p=p.next
            count+=1
        if n== count:
            return head.next   
        pos=count-n
        for i in range(pos-1):
            q=q.next
        q.next=q.next.next
        return head
