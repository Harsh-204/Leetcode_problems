class Solution:
    def maxProduct(self, n: int) -> int:
        # Convert the number to a string, then to a list of integer digits
        digits = [int(d) for d in str(n)]
        
        # Sort the list of digits in descending order
        digits.sort(reverse=True)
        
        # The maximum product will be the product of the two largest digits
        return digits[0] * digits[1]