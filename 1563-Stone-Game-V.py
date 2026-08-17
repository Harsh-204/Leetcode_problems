from functools import cache
from itertools import accumulate

class Solution:
    def stoneGameV(self, stoneValue):

        # Prefix sum
        prefix = list(accumulate(stoneValue, initial=0))

        @cache
        def dp(i, j):
            # Only one stone -> cannot split
            if i >= j:
                return 0

            ans = 0

            # Total sum of current interval
            right = prefix[j + 1] - prefix[i]
            left = 0

            for k in range(i, j):

                # Split into [i...k] and [k+1...j]
                left += stoneValue[k]
                right -= stoneValue[k]

                if left < right:
                    # Bob removes right part
                    # Alice keeps left part
                    if ans >= 2 * left:
                        continue

                    ans = max(
                        ans,
                        left + dp(i, k)
                    )

                elif left > right:
                    # Bob removes left part
                    # Alice keeps right part
                    if ans >= 2 * right:
                        break

                    ans = max(
                        ans,
                        right + dp(k + 1, j)
                    )

                else:
                    # Both sums are equal
                    ans = max(
                        ans,
                        left + dp(i, k),
                        right + dp(k + 1, j)
                    )

            return ans

        return dp(0, len(stoneValue) - 1)