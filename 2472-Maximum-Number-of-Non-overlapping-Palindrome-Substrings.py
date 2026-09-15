class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        last_end = -1  # Tracks the end index of the last chosen palindrome

        # Expand around potential centers
        for i in range(2 * n - 1):
            left = i // 2
            right = left + (i % 2)

            while left >= 0 and right < n and s[left] == s[right]:
                length = right - left + 1

                # Check if it's a valid palindrome and does not overlap with the previous selection
                if length >= k:
                    if left > last_end:
                        ans += 1
                        last_end = right
                        break  # Greedily stop expanding once the shortest valid palindrome is found

                left -= 1
                right += 1

        return ans