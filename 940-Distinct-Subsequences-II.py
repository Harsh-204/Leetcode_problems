class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = [0] * 26  # dp[i] stores count of distinct subsequences ending with char (i + 'a')
        
        for char in s:
            idx = ord(char) - ord('a')
            # 1 (for char itself) + total distinct subsequences formed so far
            dp[idx] = (sum(dp) + 1) % MOD
            
        return sum(dp) % MOD