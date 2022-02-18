# https://leetcode.com/problems/reverse-linked-list/submissions/

# Solution 1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currNode = head
        prev = None
        while currNode:
            next_node = currNode.next
            currNode.next = prev
            prev = currNode
            currNode = next_node
        return prev

# Solution 2
# With a stack


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        currNode = head
        while currNode:
            stack.append(currNode.val)
            currNode = currNode.next

        head = None
        curr = head
        n = len(stack)
        for i in range(n):
            if not head:
                head = ListNode(stack.pop(), None)
                curr = head
            else:
                curr.next = ListNode(stack.pop(), None)
                curr = curr.next
        return head
