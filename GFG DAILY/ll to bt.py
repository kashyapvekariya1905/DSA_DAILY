from tkinter.tix import Tree


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def convert(head):
    if not head:
        return None
    nodes = []
    current = head
    while current:
        nodes.append(current.data)
        current = current.next
    n = len(nodes)
    trnode = [Tree(nodes[i]) for i in range(n)]
    for i in range(n):
        li = 2 * i + 1
        ri = 2 * i + 2
        if li < n:
            trnode[i].left = trnode[li]
        if ri < n:
            trnode[i].right = trnode[ri]
    return trnode[0]
def level_order_traversal(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        result.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
root = convert(head)
print(level_order_traversal(root))
