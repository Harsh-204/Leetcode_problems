class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        res = []
        digits = "123456789"
        
        # Determine the minimum and maximum possible lengths for our range
        min_len = len(str(low))
        max_len = len(str(high))
        
        # Iterate through every possible length
        for length in range(min_len, max_len + 1):
            # Slide a window of size 'length' across the digits string
            for i in range(10 - length):
                num = int(digits[i:i + length])
                
                # If the number is within bounds, add it to our result list
                if low <= num <= high:
                    res.append(num)
                    
        return res