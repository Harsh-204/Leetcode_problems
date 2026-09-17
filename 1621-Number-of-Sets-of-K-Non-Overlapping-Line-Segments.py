class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i][j]: number of ways to form j segments using points up to index i
        dp = [[0] * (k + 1) for _ in range(n)]
        
        # Base case: 0 segments can always be formed in 1 way
        for i in range(n):
            dp[i][0] = 1
            
        for j in range(1, k + 1):
            # prefix_sum keeps track of sum(dp[p][j-1]) for all 0 <= p < i
            prefix_sum = 0
            # current_sum keeps track of sum(dp[p][j]) for all 0 <= p < i
            current_sum = 0
            
            for i in range(1, n):
                prefix_sum = (prefix_sum + dp[i - 1][j - 1]) % MOD
                current_sum = (current_sum + dp[i - 1][j]) % MOD
                
                # dp[i][j] = dp[i-1][j] + prefix_sum + current_sum
                dp[i][j] = (dp[i - 1][j] + prefix_sum + current_sum) % MOD
                
        return dp[n - 1][k]