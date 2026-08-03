class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)
        
        # Build solution backwards
        for i in range(n - 1, -1, -1):
            take1 = stoneValue[i] - dp[i + 1]
            
            take2 = float('-inf')
            if i + 1 < n:
                take2 = stoneValue[i] + stoneValue[i + 1] - dp[i + 2]
                
            take3 = float('-inf')
            if i + 2 < n:
                take3 = stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp[i + 3]
                
            dp[i] = max(take1, take2, take3)
            
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"