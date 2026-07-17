import bisect
from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        count = [0] * (max_val + 1)
        
        # Step 1: Count frequency of each number
        for num in nums:
            count[num] += 1
        
        gcd_cnt = [0] * (max_val + 1)
        
        # Step 2 & 3: Find exact count of pairs for each GCD
        for g in range(max_val, 0, -1):
            c = 0
            # Count how many multiples of g are in nums
            for multiple in range(g, max_val + 1, g):
                c += count[multiple]
            
            # Number of pairs where both numbers are multiples of g
            pairs = c * (c - 1) // 2
            
            # Subtract pairs where the exact GCD is a greater multiple of g
            for multiple in range(2 * g, max_val + 1, g):
                pairs -= gcd_cnt[multiple]
            
            gcd_cnt[g] = pairs
        
        # Step 4: Compute prefix sums of the GCD counts
        prefix_sums = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix_sums[i] = prefix_sums[i - 1] + gcd_cnt[i]
        
        # Step 5: Answer each query using binary search
        ans = []
        for q in queries:
            # Find the first index i such that prefix_sums[i] > q
            idx = bisect.bisect_right(prefix_sums, q)
            ans.append(idx)
            
        return ans