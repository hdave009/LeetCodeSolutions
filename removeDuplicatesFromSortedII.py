# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Solution 1 : Working on it
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lastDistinct = None
        currNode = head
        while currNode.next:
            print(currNode.val)
            if currNode.val != currNode.next.val:
                if lastDistinct:
                    lastDistinct.next = currNode
                    currNode = currNode.next
                else:
                    head = currNode
                    lastDistinct = currNode
                    currNode = currNode.next
            else:
                val = currNode.val
                while currNode.val == val:
                    currNode = currNode.next
        return head

# Solution 2 :  Wokring on it
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lastDistinct = None
        currNode = head
        while currNode:
            if currNode.next and currNode.next.val == currNode.val:
                while currNode.next and currNode.next.val == currNode.val:
                    currNode = currNode.next
                currNode = currNode.next
            else:
                if lastDistinct:
                    lastDistinct.next = currNode
                else:
                    lastDistinct = currNode
                    head = lastDistinct
                currNode = currNode.next
        return head
