# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        p=head
        q=head
        count=1
        while p.next!=None:
            p=p.next
            count+=1
        mid=(count//2)
        left=0
        while left<mid:
            q=q.next
            left+=1
        head=q
        return head