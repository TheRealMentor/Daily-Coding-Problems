#Have not tried it yet!!!
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
def delNthLastNode(head, k):
    curr_ptr, main_ptr = head, head
    cnt = 0

    #Traversing till the kth last element
    while cnt < k:
        curr_ptr = curr_ptr.next
        cnt += 1
    
    while curr_ptr:
        main_ptr = main_ptr.next
        curr_ptr = curr_ptr.next
    
    #Deleting the kth last element
    curr_ptr = main_ptr
    curr_ptr.val = curr_ptr.next.val
    curr_ptr = curr_ptr.next

    while curr_ptr.next:
        curr_ptr.val = curr_ptr.next.val
        main_ptr = curr_ptr
        curr_ptr = curr_ptr.next
    
    main_ptr.next = None
