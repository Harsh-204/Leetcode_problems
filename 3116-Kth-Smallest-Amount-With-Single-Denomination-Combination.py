import math
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        
        # Precompute the LCM and the PIE sign for all non-empty subsets of coins
        subsets = []
        for i in range(1, 1 << n):
            current_lcm = 1
            set_bits = 0
            for j in range(n):
                if i & (1 << j):
                    set_bits += 1
                    current_lcm = math.lcm(current_lcm, coins[j])
            
            # Odd number of coins -> Add (sign 1)
            # Even number of coins -> Subtract (sign -1)
            sign = 1 if set_bits % 2 == 1 else -1
            subsets.append((current_lcm, sign))
            
        def count_amounts_up_to(x):
            # Calculate how many valid amounts are <= x using PIE
            count = 0
            for lcm_val, sign in subsets:
                count += sign * (x // lcm_val)
            return count

        # Binary search range
        left = 1
        right = min(coins) * k
        
        while left <= right:
            mid = (left + right) // 2
            
            if count_amounts_up_to(mid) >= k:
                # mid might be the answer, but try to find a smaller valid one
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return ans