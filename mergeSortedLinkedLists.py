# https://leetcode.com/problems/merge-two-sorted-lists/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode()
        curr = new_list
        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    curr.next, list1 = list1, list1.next
                else:
                    curr.next, list2 = list2, list2.next
                if not new_list:
                    new_list = curr
                curr = curr.next
            elif list1 and not list2:
                curr.next = list1
                break
            else:
                curr.next = list2
                break
        return new_list.next
