class Solution:

    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, ch in enumerate(s, start=1):
            rev_alphabet_idx = 26 - (ord(ch) - ord("a"))
            total += rev_alphabet_idx * i
        return total