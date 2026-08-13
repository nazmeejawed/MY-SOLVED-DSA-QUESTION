from typing import List

class SegmentTree:
    def __init__(self, s: str):
        self.n = len(s)
        self.s = list(s)
        self.tree_max = [0] * (4 * self.n)
        self.tree_pref = [0] * (4 * self.n)
        self.tree_suff = [0] * (4 * self.n)
        self.tree_lc = [''] * (4 * self.n)
        self.tree_rc = [''] * (4 * self.n)
        self.build(1, 0, self.n - 1)

    def merge(self, node: int, left_child: int, right_child: int, l_len: int, r_len: int):
        lc_l = self.tree_lc[left_child]
        rc_l = self.tree_rc[left_child]
        lc_r = self.tree_lc[right_child]
        rc_r = self.tree_rc[right_child]

        self.tree_lc[node] = lc_l
        self.tree_rc[node] = rc_r

        # Maximum inside either sub-tree
        self.tree_max[node] = max(self.tree_max[left_child], self.tree_max[right_child])
        
        # Merge Prefix
        self.tree_pref[node] = self.tree_pref[left_child]
        if self.tree_pref[left_child] == l_len and rc_l == lc_r:
            self.tree_pref[node] = l_len + self.tree_pref[right_child]

        # Merge Suffix
        self.tree_suff[node] = self.tree_suff[right_child]
        if self.tree_suff[right_child] == r_len and rc_l == lc_r:
            self.tree_suff[node] = r_len + self.tree_suff[left_child]

        # Crossing boundary update
        if rc_l == lc_r:
            self.tree_max[node] = max(
                self.tree_max[node], 
                self.tree_suff[left_child] + self.tree_pref[right_child]
            )

    def build(self, node: int, start: int, end: int):
        if start == end:
            char = self.s[start]
            self.tree_max[node] = 1
            self.tree_pref[node] = 1
            self.tree_suff[node] = 1
            self.tree_lc[node] = char
            self.tree_rc[node] = char
            return
        
        mid = (start + end) // 2
        left_child = 2 * node
        right_child = 2 * node + 1
        
        self.build(left_child, start, mid)
        self.build(right_child, mid + 1, end)
        
        self.merge(node, left_child, right_child, mid - start + 1, end - mid)

    def update(self, node: int, start: int, end: int, idx: int, char: str):
        if start == end:
            self.tree_max[node] = 1
            self.tree_pref[node] = 1
            self.tree_suff[node] = 1
            self.tree_lc[node] = char
            self.tree_rc[node] = char
            return

        mid = (start + end) // 2
        left_child = 2 * node
        right_child = 2 * node + 1

        if idx <= mid:
            self.update(left_child, start, mid, idx, char)
        else:
            self.update(right_child, mid + 1, end, idx, char)

        self.merge(node, left_child, right_child, mid - start + 1, end - mid)

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        st = SegmentTree(s)
        ans = []
        for char, idx in zip(queryCharacters, queryIndices):
            st.update(1, 0, st.n - 1, idx, char)
            ans.append(st.tree_max[1])
        return ans