# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1=l1
        p2=l2
        num1=""
        while p1!=None:
            num1+=str(p1.val)
            p1=p1.next
        num2=""
        while(p2!=None):
            num2+=str(p2.val)
            p2=p2.next
        num1=num1[::-1]
        num2=num2[::-1]
        n1=int(num1)
        n2=int(num2)

        s=n1+n2

        summ=str(s)
        summ=summ[::-1]


        l3 = ListNode(int(summ[0]))
        curr = l3
        for i in range(1,len(summ)):
            curr.next=ListNode(int(summ[i]))
            curr=curr.next
        return l3
