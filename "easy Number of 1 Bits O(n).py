def hammingWeight(self, n: int) -> int:
    bit = 0

    while n:
        bit += 1
        n &= n - 1

    return bit
