# https://leetcode.com/problems/linked-list-cycle-ii/submissions/

# Solution 1
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = []
        while head:
            if head in seen:
                return head
            seen.append(head)
            head = head.next
        return None
