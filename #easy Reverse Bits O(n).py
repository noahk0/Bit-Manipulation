def reverseBits(self, n: int) -> int:
    bit = n % 2

    for _ in range(31):
        n //= 2
        bit += bit + n % 2

    return bit
