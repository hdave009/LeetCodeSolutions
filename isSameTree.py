# https://leetcode.com/problems/same-tree/

# My Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif p and q and p.val == q.val:
            return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
        else:
            return False

# My Solution 2 - Breadth First Search


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # BFS
        if not p and not q:
            return True

        p_q = deque([p])
        q_q = deque([q])
        while p_q and q_q:
            if len(p_q) != len(q_q):
                return False
            for i in range(len(p_q)):
                p_node = p_q.popleft()
                q_node = q_q.popleft()
                if ((p_node or q_node) and not (p_node and q_node)) or (p_node and q_node and p_node.val != q_node.val):
                    return False
                if p_node:
                    p_q.extend([p_node.right, p_node.left])
                    q_q.extend([q_node.right, q_node.left])

        return True

# My Solution 2 - Iterative DFS


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # DFS
        stack = [[p, q]]
        while stack:
            top = stack.pop()
            if ((not top[0] or not top[1]) and (top[0] or top[1])) or (top[0] and top[1] and top[0].val != top[1].val):
                return False
            if top[0]:
                stack.append([top[0].right, top[1].right])
                stack.append([top[0].left, top[1].left])
        return True
