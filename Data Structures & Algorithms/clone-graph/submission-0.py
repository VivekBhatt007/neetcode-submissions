"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return node
        
        def dfsHelper(node, visited) -> Optional['Node']:
            if node in visited:
                return visited[node]

            newNode = Node(node.val)
            visited[node] = newNode
            for n in node.neighbors:
                newNode.neighbors.append(dfsHelper(n, visited))
            return newNode
        
        return dfsHelper(node, {})


        