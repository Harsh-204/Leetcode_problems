class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq = [0] * 26
        visited = [False] * 26

        # Count frequency of each character
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        stack = []

        for ch in s:
            idx = ord(ch) - ord('a')
            freq[idx] -= 1

            if visited[idx]:
                continue

            while (stack and
                   stack[-1] > ch and
                   freq[ord(stack[-1]) - ord('a')] > 0):
                visited[ord(stack.pop()) - ord('a')] = False

            stack.append(ch)
            visited[idx] = True

        return "".join(stack)