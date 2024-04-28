# 24. Swap Nodes in Pairs
# Medium
# Topics
# Companies
# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

# Example 1:


# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# Example 2:

# Input: head = []
# Output: []
# Example 3:

# Input: head = [1]
# Output: [1]
 

# Constraints:

# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100

from typing import List, Optional

class Listnode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
      

class Solution:
    def swapnodes(self, head:Optional[Listnode]) -> Optional[Listnode]:
        dummy = Listnode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            nextpair = curr.next.next
            second = curr.next

            second.next = curr
            curr.next = nextpair
            prev.next = second

            prev = curr
            curr = nextpair

        return dummy.next

def create_linked_list(values):
    dummy = Listnode()
    current = dummy
    for value in values:
        current.next = Listnode(value)
        current = current.next
    return dummy.next

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()


sol = Solution()
L = [1,2,3,4]
head = create_linked_list(L)
print_linked_list(sol.swapnodes(head))