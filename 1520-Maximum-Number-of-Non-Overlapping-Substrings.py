class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # Step 1: Record the first and last occurrence of each character
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        valid_substrings = []

        # Step 2: Find all valid intervals starting from each character's first appearance
        for ch in first:
            i = first[ch]
            j = last[ch]
            is_valid = True
            k = i

            while k <= j:
                c = s[k]
                # If a character inside the range starts before 'i',
                # 'i' cannot be the start of a valid range.
                if first[c] < i:
                    is_valid = False
                    break
                j = max(j, last[c])
                k += 1

            if is_valid:
                valid_substrings.append((i, j))

        # Step 3: Sort valid intervals by ending index (greedy selection)
        valid_substrings.sort(key=lambda x: x[1])

        res = []
        last_end = -1

        for start, end in valid_substrings:
            if start > last_end:
                res.append(s[start : end + 1])
                last_end = end

        return res