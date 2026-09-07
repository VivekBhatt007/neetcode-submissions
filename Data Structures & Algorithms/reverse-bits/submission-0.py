class Solution:
    def reverseBits(self, n: int) -> int:
        out = 0
        for i in range(32):
            t = (n >> i) & 1
            out |= (t & 1) << (31 -i)
        return out
        