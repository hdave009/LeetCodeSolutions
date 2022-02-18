# https://leetcode.com/problems/linked-list-cycle/submissions/

# Solution 1
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        return self.hasCycleRec(head, [])

    def hasCycleRec(self, head, seen):
        if not head:
            return False
        elif head in seen:
            return True
        else:
            seen.append(head)
            return self.hasCycleRec(head.next, seen)

# Solution 2


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = []
        while head:
            if head in seen:
                return True
            seen.append(head)
            head = head.next
        return False


# Solution 3
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while True:
            fast = fast.next.next if fast and fast.next else None
            if not fast:
                return False
            slow = slow.next
            if slow == fast:
                return True
