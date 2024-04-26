# 19. Remove Nth Node From End of List

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

from typing import List 
from typing import Optional

class ListNode:
    def __init__(self, value = 0, next = None):
        self.val = value
        self.next = next

class Solution:
    def removeNthnode(self, head: Optional[ListNode], n:int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        for _ in range(n+1):
            first = first.next
        
        while first is not None:
            first = first.next
            second = second.next
        
        second.next = second.next.next

        return dummy.next
    

def create_linked_list(elements):
    head = ListNode(elements[0])
    current = head
    for element in elements[1:]:
        current.next = ListNode(element)
        current = current.next
    return head

sol = Solution()
L = create_linked_list([1,2,3,4,5,6,7,8,6,7,8,9])

def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

print_linked_list(sol.removeNthnode(L,4))



