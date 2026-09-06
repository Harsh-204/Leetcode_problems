class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0
        
        # dp[j] stores the number of distinct subsequences of s that equal t[:j]
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: empty string t can always be formed 1 way
        
        for char in s:
            for j in range(n, 0, -1):
                if char == t[j - 1]:
                    dp[j] += dp[j - 1]
                    
        return dp[n]