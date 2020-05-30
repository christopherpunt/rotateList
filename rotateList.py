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


#old rotate method with complexity of O(n^2)    
def oldrotate(head, k):
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


#new rotate method with complexity O(n)
def rotate(head, k):
    if (head is None):
        return head

    temp = head
    length = 1
    #loop until we reach the kth Node to get the length of the list
    while (temp.next is not None):
        temp = temp.next
        length += 1

    #if k is greater than the size of the list
    if (k > length):
        k = k % length

    #needed to reverse the rotation
    k = length - k
    
    #if a rotation is not needed
    if (k == 0):
        return head

    current = head
    count = 1
    while(count < k and current.next is not None):
        current = current.next
        count += 1

    #new kth node set to current
    kNode = current

    #changing the next node of the previous head
    temp.next = head

    #changing the head to the k+1 node
    head = kNode.next

    #set the next node of the kth Node to None
    kNode.next = None
        
    return head   
    

#test cases

#1,2,3,4,5 k=1
print("1,2,3,4,5 k=1")
head0 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
print(oldrotate(head0, 1))
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))      
print(rotate(head1, 1))
print()

#1,2,3,4,5 k=2
print("1,2,3,4,5 k=2")
head0 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
print(oldrotate(head0, 2))
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))      
print(rotate(head1, 2))
print()

#1,2,3,4,5 k=36
print("1,2,3,4,5 k=36")
head0 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
print(oldrotate(head0, 36))
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))      
print(rotate(head1, 36))
print()

#0,1,2 k=1
print("0,1,2 k=1")
head0 = ListNode(0, ListNode(1, ListNode(2, None)))
print(oldrotate(head0, 1))
head1 = ListNode(0, ListNode(1, ListNode(2, None)))
print(rotate(head1, 1))
print()

#0,1,2 k=2
print("0,1,2 k=2")
head0 = ListNode(0, ListNode(1, ListNode(2, None)))
print(oldrotate(head0, 2))
head1 = ListNode(0, ListNode(1, ListNode(2, None)))
print(rotate(head1, 2))
print()

#0,1,2 k=3
print("0,1,2 k=3")
head0 = ListNode(0, ListNode(1, ListNode(2, None)))
print(oldrotate(head0, 3))
head1 = ListNode(0, ListNode(1, ListNode(2, None)))
print(rotate(head1, 3))
print()

#0,1,2 k=4
print("0,1,2 k=4")
head0 = ListNode(0, ListNode(1, ListNode(2, None)))
print(oldrotate(head0, 4))
head1 = ListNode(0, ListNode(1, ListNode(2, None)))
print(rotate(head1, 4))
print()