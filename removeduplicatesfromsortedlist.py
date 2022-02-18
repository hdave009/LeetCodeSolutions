# https: // leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/

# Solution 1


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = head
        current = head.next if head else None
        while last and current:
            if current.val == last.val:
                current = current.next
            else:
                last.next = current
                last = current
        if last:
            last.next = None
        return head
