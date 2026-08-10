class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # dp[i] will be True if the current player can win with i stones
        dp = [False] * (n + 1)
        
        for i in range(1, n + 1):
            k = 1
            # Check all possible valid square numbers we can remove
            while k * k <= i:
                # If removing k*k stones leaves the opponent with a losing state, 
                # then the current player wins from state i.
                if not dp[i - k * k]:
                    dp[i] = True
                    break
                k += 1
                
        return dp[n]