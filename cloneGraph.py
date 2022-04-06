# https://leetcode.com/problems/clone-graph/submissions/

# Solution 1
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node:
            return self.cloneGraphRec(node, {})
        return None

    def cloneGraphRec(self, node: 'Node', visited) -> 'Node':
        new_node = Node(node.val, [])
        visited[node.val] = new_node
        for n in node.neighbors:
            if n.val in visited:
                new_node.neighbors.append(visited[n.val])
            else:
                new_node.neighbors.append(self.cloneGraphRec(n, visited))
        return new_node
