class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Build adjacency list for the directed invocation graph
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)
        
        # Identify all suspicious methods reachable from node k
        suspicious = set([k])
        stack = [k]
        
        while stack:
            curr = stack.pop()
            for neighbor in graph[curr]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    stack.append(neighbor)
        
        # Check if any non-suspicious method calls a suspicious method
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))
        
        # If no external invocation exists, return all non-suspicious methods
        return [i for i in range(n) if i not in suspicious]