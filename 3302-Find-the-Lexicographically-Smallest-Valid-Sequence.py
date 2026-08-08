class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n, m = len(word1), len(word2)
        
        # suf[i] stores the length of the longest suffix of word2 
        # that can be exactly matched as a subsequence in word1[i:]
        suf = [0] * (n + 1)
        j = m - 1
        
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                suf[i] = suf[i + 1] + 1
                j -= 1
            else:
                suf[i] = suf[i + 1]
                
        ans = []
        j = 0
        changed = False
        
        # Greedily find the earliest matching indices
        for i in range(n):
            if j == m:
                break
                
            # If characters match exactly, we take the index
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            # If they don't match, we check if we can safely use our single change
            elif not changed and suf[i + 1] >= m - 1 - j:
                ans.append(i)
                changed = True
                j += 1
                
        return ans if len(ans) == m else []