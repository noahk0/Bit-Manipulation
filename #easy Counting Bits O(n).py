def countBits(self, n: int) -> List[int]:
    bit = [0]

    for i in range(1, n + 1):
        bit.append(bit[i // 2] + i % 2)

    return bit
