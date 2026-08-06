class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        # Loop indefinitely until we find the matching number
        while True:
            temp = n
            digit_product = 1
            
            # Calculate the product of the digits
            while temp > 0:
                digit_product *= temp % 10
                temp //= 10
                
            # Check if the product is divisible by t
            if digit_product % t == 0:
                return n
                
            # Increment n to check the next number
            n += 1