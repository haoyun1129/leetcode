class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            if n == 0:
                res <<= (32-i)
                break
            res <<= 1
            res |= (n & 1)
            n >>= 1
        return res

s = Solution()
print(s.reverseBits(int("00000010100101000001111010011100", 2)))  # 00111001011110000010100101000000
print(s.reverseBits(int("11111111111111111111111111111101", 2)))  # 10111111111111111111111111111111
