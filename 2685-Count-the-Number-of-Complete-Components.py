import collections
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build the adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = [False] * n
        complete_components = 0
        
        for i in range(n):
            if not visited[i]:
                # Start a new component traversal using BFS
                q = collections.deque([i])
                visited[i] = True
                
                nodes_count = 0
                sum_of_degrees = 0
                
                while q:
                    curr = q.popleft()
                    nodes_count += 1
                    sum_of_degrees += len(adj[curr])
                    
                    for neighbor in adj[curr]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            q.append(neighbor)
                
                # A complete graph of V nodes has V*(V-1)/2 edges.
                # Since sum_of_degrees is 2 * edges, it must equal V * (V - 1)
                if sum_of_degrees == nodes_count * (nodes_count - 1):
                    complete_components += 1
                    
        return complete_components