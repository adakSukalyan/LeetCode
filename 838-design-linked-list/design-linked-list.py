class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head=None
        self.size=0

    def get(self, index: int) -> int:
        if index<0 or index>= self.size:
            return -1
        p=self.head
        for i in range(index):
            p=p.next
        return p.val

    def addAtHead(self, val: int) -> None:
        new=Node(val)
        new.next=self.head
        self.head=new
        self.size+=1

    def addAtTail(self, val: int) -> None:
        new=Node(val)
        if not self.head:
            self.head=new
        else:
            p=self.head
            while p.next!=None:
                p=p.next
            p.next=new
        self.size+=1

    def addAtIndex(self, index: int, val: int) -> None:
        new=Node(val)
        if index<0:
            index=0
        if index> self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        p=self.head
        for i in range(index-1):
            p=p.next
        new.next=p.next
        p.next=new
        self.size+=1
    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return None
        if index<0 or index>=self.size:
            return
        if index==0:
            self.head=self.head.next
        else:
            p=self.head
            for i in range(index-1):
                if not p.next:
                    return None
                p=p.next
            p.next=p.next.next
        self.size-=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)