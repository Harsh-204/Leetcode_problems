import math

class Solution:
    def subsequencePairCount(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        
        # dp stores the mapping: (gcd1, gcd2) -> count
        # (0, 0) represents the state where both subsequences are empty.
        dp = {(0, 0): 1}
        
        for x in nums:
            # Create a copy of the current dp state to represent the option 
            # where we do NOT include 'x' in either subsequence.
            next_dp = dp.copy()
            
            for (g1, g2), count in dp.items():
                # Option 1: Add 'x' to the first subsequence
                ng1 = math.gcd(g1, x)
                next_dp[(ng1, g2)] = (next_dp.get((ng1, g2), 0) + count) % MOD
                
                # Option 2: Add 'x' to the second subsequence
                ng2 = math.gcd(g2, x)
                next_dp[(g1, ng2)] = (next_dp.get((g1, ng2), 0) + count) % MOD
                
            dp = next_dp
            
        # Sum up all configurations where both subsequences are non-empty
        # (meaning their GCDs are > 0) and their GCDs are equal.
        ans = 0
        for (g1, g2), count in dp.items():
            if g1 > 0 and g1 == g2:
                ans = (ans + count) % MOD
                
        return ans