# https://leetcode.com/problems/add-two-numbers/submissions/

# Solution 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_list = None
        place = sum_list
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry = (val1 + val2) // 10
            val = (val1 + val2) - (carry * 10)
            ans_node = ListNode(val, None)
            if not sum_list:
                sum_list = ans_node
                place = sum_list
            else:
                place.next = ans_node
                place = place.next
            if l1 and l1.next:
                l1.next.val += carry
            elif l2 and l2.next:
                l1.next = ListNode(carry, None)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            place.next = ListNode(carry, None)
        return sum_list
