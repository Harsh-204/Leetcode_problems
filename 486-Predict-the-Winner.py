class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        # dp[i][j] stores the max score difference for subarray nums[i...j]
        dp = [[0] * n for _ in range(n)]
        
        # Base case: subarray of length 1
        for i in range(n):
            dp[i][i] = nums[i]
            
        # Build the table for subarrays of length 2 to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                pick_left = nums[i] - dp[i + 1][j]
                pick_right = nums[j] - dp[i][j - 1]
                dp[i][j] = max(pick_left, pick_right)
                
        # Player 1 wins if the score difference is >= 0
        return dp[0][n - 1] >= 0