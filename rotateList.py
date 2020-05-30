# Given a linked list, rotate the list to the right by k places, where k is non-negative.
# 
# Example 1:
# 
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL
# Example 2:
# 
# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return '%s -> %s' % (self.val, self.next)
    

    
def rotate(head, k):
    if k == 0:
        return head
    
    previous = None
    current = head
    
    
    for i in range(k):
        while(current.next is not None):
            previous = current
            current = current.next
        previous.next = None
        current.next = head
        head = current
        
    return head


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))      
print(rotate(head, 36))