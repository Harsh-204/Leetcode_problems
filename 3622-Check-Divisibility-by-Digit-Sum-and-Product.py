class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_prod = 1
        
        # Iterate through each digit in the number
        for d in str(n):
            digit = int(d)
            digit_sum += digit
            digit_prod *= digit
            
        # Check if n is divisible by their sum
        return n % (digit_sum + digit_prod) == 0