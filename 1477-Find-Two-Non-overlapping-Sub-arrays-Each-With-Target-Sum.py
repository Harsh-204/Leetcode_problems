class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        dp = [float('inf')] * n
        
        left = 0
        window_sum = 0
        min_sum_len = float('inf')
        min_len_so_far = float('inf')
        
        for right in range(n):
            window_sum += arr[right]
            
            # Shrink window if sum exceeds target
            while window_sum > target:
                window_sum -= arr[left]
                left += 1
                
            # Valid subarray found
            if window_sum == target:
                curr_len = right - left + 1
                
                # Check if there is a non-overlapping valid subarray to the left
                if left > 0 and dp[left - 1] != float('inf'):
                    min_sum_len = min(min_sum_len, dp[left - 1] + curr_len)
                
                min_len_so_far = min(min_len_so_far, curr_len)
            
            dp[right] = min_len_so_far
            
        return min_sum_len if min_sum_len != float('inf') else -1