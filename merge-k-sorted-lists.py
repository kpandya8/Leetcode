# 23. Merge k Sorted Lists
# Hard
# Topics
# Companies
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

 

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []
 

# Constraints:

# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        mid = len(lists) // 2
        left_merged = self.mergeKLists(lists[:mid])
        right_merged = self.mergeKLists(lists[mid:])
        
        return self.mergeTwoLists(left_merged, right_merged)

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
            
        if l1:
            current.next = l1
        elif l2:
            current.next = l2
        
        return dummy.next

def convert_to_linked_list(nums):
    dummy = ListNode()
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Input preparation
input_lists = [[1,4,5],[1,3,4],[2,6]]
linked_lists = [convert_to_linked_list(l) for l in input_lists]

# Solution instantiation and method call
sol = Solution()
merged_head = sol.mergeKLists(linked_lists)

# Function to print the linked list
def print_linked_list(node):
    while node:
        print(node.val, end=' -> ' if node.next else '')
        node = node.next
    print()

print_linked_list(merged_head)
