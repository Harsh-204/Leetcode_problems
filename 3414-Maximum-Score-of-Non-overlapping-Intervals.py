from bisect import bisect_right
from functools import lru_cache
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        # Store (l, r, weight, original_index)
        arr = sorted((l, r, w, i) for i, (l, r, w) in enumerate(intervals))
        starts = [x[0] for x in arr]
        
        # dp[i][k] stores (max_weight, list_of_indices)
        # We work backwards from n to 0 to easily compute lexicographically best results
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            l, r, w, idx = arr[i]
            # Find next non-overlapping interval
            next_idx = bisect_right(starts, r)
            
            for k in range(1, 5):
                # Option 1: Skip interval i
                best_w, best_res = dp[i + 1][k]
                
                # Option 2: Take interval i
                next_w, next_res = dp[next_idx][k - 1]
                take_w = w + next_w
                take_res = sorted([idx] + next_res)
                
                # Compare Take vs Skip
                if take_w > best_w:
                    best_w, best_res = take_w, take_res
                elif take_w == best_w and take_w > 0:
                    if not best_res or take_res < best_res:
                        best_res = take_res
                        
                dp[i][k] = (best_w, best_res)
                
        # Best overall solution starting from index 0 across all k in [1..4]
        max_w = -1
        res = []
        for k in range(1, 5):
            w, indices = dp[0][k]
            if w > max_w:
                max_w = w
                res = indices
            elif w == max_w and w > 0:
                if indices < res:
                    res = indices
                    
        return res