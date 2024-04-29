# 25. Reverse Nodes in k-Group
# Hard
# Topics
# Companies
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Example 2:


# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
 

# Constraints:

# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000
 

# Follow-up: Can you solve the problem in O(1) extra memory space?

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = prevEnd = ListNode(next=head)
        curr = currEnd = head
        prev = None
        cnt = 1
        while curr:
            curr.next,prev,curr = prev,curr,curr.next
            if cnt%k==0:
                prevEnd.next,prevEnd,currEnd,prev = prev,currEnd,curr,None
            cnt += 1

        curr = prev
        prev = None
        while curr:
            curr.next,prev,curr = prev,curr,curr.next
        prevEnd.next = prev

        return dummy.next
    def get_kth_node(self, start, k):
        while k > 0 and start:
            start = start.next
            k -= 1
        return start

def list_to_linked_list(elements):
    dummy = ListNode(0)
    current = dummy
    for element in elements:
        current.next = ListNode(element)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    elements = []
    while head:
        elements.append(head.val)
        head = head.next
    return elements

# Example Usage
elements = [1, 2, 3, 4, 5]
k = 2
head = list_to_linked_list(elements)
sol = Solution()
result_head = sol.reverseKGroup(head, k)
result = linked_list_to_list(result_head)
print(result)