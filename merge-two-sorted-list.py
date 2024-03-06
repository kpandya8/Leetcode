from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next

# Helper function to convert a list to a linked list
def list_to_linked_list(elements):
    head = ListNode(0)
    current = head
    for element in elements:
        current.next = ListNode(element)
        current = current.next
    return head.next

# Helper function to print a linked list
def print_linked_list(node):
    elements = []
    while node:
        elements.append(node.val)
        node = node.next
    print(elements)

# Test the solution
list1 = list_to_linked_list([1,2,4])
list2 = list_to_linked_list([1,3,4])
sol = Solution()
result = sol.mergeTwoLists(list1, list2)

print_linked_list(result)  # This should print the merged list
