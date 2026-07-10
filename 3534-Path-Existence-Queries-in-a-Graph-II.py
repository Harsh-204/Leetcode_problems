import bisect
from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # Pair each number with its original index and sort by value
        sorted_nodes = sorted((val, idx) for idx, val in enumerate(nums))
        sorted_vals = [val for val, idx in sorted_nodes]
        
        # Map original index to its position in the sorted array
        pos = {idx: i for i, (val, idx) in enumerate(sorted_nodes)}
        
        # Binary lifting setup
        LOG = 18
        up = [[n] * LOG for _ in range(n + 1)]
        
        # Determine the greedy next jump for each node in sorted order
        for i in range(n):
            val = sorted_vals[i]
            # Find the furthest possible index to the right within maxDiff
            target_idx = bisect.bisect_right(sorted_vals, val + maxDiff) - 1
            if target_idx > i:
                up[i][0] = target_idx
            else:
                up[i][0] = n
                
        up[n][0] = n
        
        # Fill the binary lifting table
        for j in range(1, LOG):
            for i in range(n + 1):
                up[i][j] = up[up[i][j-1]][j-1]
                
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            if nums[u] == nums[v]:
                if abs(nums[u] - nums[v]) <= maxDiff: # checking reachability constraint
                    ans.append(1)
                else:
                    ans.append(-1)
                continue
                
            p_u, p_v = pos[u], pos[v]
            if p_u > p_v:
                p_u, p_v = p_v, p_u
                
            target_val = sorted_vals[p_v]
            
            # Greedily lift p_u towards p_v without exceeding target_val
            curr = p_u
            steps = 0
            for j in range(LOG - 1, -1, -1):
                nxt = up[curr][j]
                if nxt != n and sorted_vals[nxt] <= target_val:
                    curr = nxt
                    steps += (1 << j)
            
            # If we reached p_v or a valid node with the same value destination
            if sorted_vals[curr] == target_val:
                ans.append(steps)
            elif up[curr][0] != n and up[curr][0] >= p_v:
                ans.append(steps + 1)
            else:
                ans.append(-1)
                
        return ans