# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = root
        if p.val > q.val:
            p, q = q, p
        while lca:
            if p.val <= lca.val and lca.val <= q.val:
                return lca
            elif p.val < lca.val:
                lca = lca.left
            else:
                lca = lca.right
