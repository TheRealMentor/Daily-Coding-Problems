class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def linkedListInter(head1, head2):
    c1 = countNodes(head1)
    c2 = countNodes(head2)

    if c1 >= c2:
        d = c1-c2
        curr1 = head1
        curr2 = head2
    else:
        d = c2-c1
        curr1 = head2
        curr2 = head1

    for _ in range(d):
        if curr1 == None:
            return -1
        curr1 = curr1.next
    
    while curr1 != None and curr2 != None:
        if curr1.val == curr2.val:
            return curr1.val
        curr1 = curr1.next
        curr2 = curr2.next
    
    return -1

def countNodes(head):
    curr = head
    cnt = 0

    while curr != None:
        cnt += 1
        curr = curr.next
    
    return cnt

llist1 = Node(3)
llist1.next = Node(6)
llist1.next.next = Node(9)
llist1.next.next.next = Node(15)
llist1.next.next.next.next = Node(30)

llist2 = Node(10)
llist2.next = Node(16)
llist2.next.next = Node(30)

print(linkedListInter(llist1, llist2))