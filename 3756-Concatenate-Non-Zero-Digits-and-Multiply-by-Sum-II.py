class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        ans = []

        for l, r in queries:
            x = 0
            digit_sum = 0

            for ch in s[l:r + 1]:
                if ch != '0':
                    digit = int(ch)
                    x = (x * 10 + digit) % MOD
                    digit_sum += digit

            ans.append((x * digit_sum) % MOD)

        return ans