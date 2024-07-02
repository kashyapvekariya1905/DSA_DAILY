from lib2to3.pytree import Node


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head) -> ListNode:
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    current = head

    while current:
        check = False
        while current.next and current.data == current.next.data:
            check = True
            current = current.next
        if check:
            prev.next = current.next
        else:
            prev = prev.next
        current = current.next
    
    return dummy.next
def printList(head: ListNode):
    current = head
    while current:
        print(current.val, end=' ')
        current = current.next
    print()
head = ListNode(23)
head.next = ListNode(28)
head.next.next = ListNode(28)
head.next.next.next = ListNode(35)
head.next.next.next.next = ListNode(49)
head.next.next.next.next.next = ListNode(49)
head.next.next.next.next.next.next = ListNode(53)
head.next.next.next.next.next.next.next = ListNode(53)
result = deleteDuplicates(head)
printList(result)  # Output: 23 35
