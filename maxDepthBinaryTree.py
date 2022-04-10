# https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/

# Solution 1 - My Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maxDepthRec(root, longest=0):
            if not root:
                return longest
            elif not root.left and not root.right:
                return longest + 1
            elif root.right and not root.left:
                return maxDepthRec(root.right, longest + 1)
            elif root.left and not root.right:
                return maxDepthRec(root.left, longest + 1)
            else:
                return max(maxDepthRec(root.right, longest + 1), maxDepthRec(root.left, longest + 1))
        return maxDepthRec(root)

    # Recursive DFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))

    # Iterative DFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node:
                stack.append([node.right, depth + 1])
                stack.append([node.left, depth + 1])
                res = max(res, depth)
        return res

    # BFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
