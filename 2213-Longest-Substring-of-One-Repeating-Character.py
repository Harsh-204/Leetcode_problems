class Node:
    __slots__ = ('pref', 'suff', 'mx', 'lc', 'rc')
    def __init__(self, pref=1, suff=1, mx=1, lc='', rc=''):
        self.pref = pref
        self.suff = suff
        self.mx = mx
        self.lc = lc
        self.rc = rc

class SegmentTree:
    def __init__(self, s: str):
        self.n = len(s)
        self.tree = [Node() for _ in range(4 * self.n)]
        self.build(s, 0, 0, self.n - 1)

    def merge(self, left: Node, right: Node, len_l: int, len_r: int) -> Node:
        res = Node()
        res.lc = left.lc
        res.rc = right.rc

        res.mx = max(left.mx, right.mx)
        res.pref = left.pref
        res.suff = right.suff

        # Check if boundary characters match
        if left.rc == right.lc:
            res.mx = max(res.mx, left.suff + right.pref)
            if left.pref == len_l:
                res.pref = len_l + right.pref
            if right.suff == len_r:
                res.suff = len_r + left.suff

        return res

    def build(self, s: str, node: int, l: int, r: int):
        if l == r:
            ch = s[l]
            self.tree[node] = Node(1, 1, 1, ch, ch)
            return
        
        mid = (l + r) // 2
        lc, rc = 2 * node + 1, 2 * node + 2
        self.build(s, lc, l, mid)
        self.build(s, rc, mid + 1, r)
        self.tree[node] = self.merge(self.tree[lc], self.tree[rc], mid - l + 1, r - mid)

    def update(self, node: int, l: int, r: int, idx: int, ch: str):
        if l == r:
            self.tree[node] = Node(1, 1, 1, ch, ch)
            return

        mid = (l + r) // 2
        lc, rc = 2 * node + 1, 2 * node + 2
        if idx <= mid:
            self.update(lc, l, mid, idx, ch)
        else:
            self.update(rc, mid + 1, r, idx, ch)
            
        self.tree[node] = self.merge(self.tree[lc], self.tree[rc], mid - l + 1, r - mid)

    def query_max(self) -> int:
        return self.tree[0].mx

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        st = SegmentTree(s)
        ans = []
        
        for ch, idx in zip(queryCharacters, queryIndices):
            st.update(0, 0, len(s) - 1, idx, ch)
            ans.append(st.query_max())
            
        return ans