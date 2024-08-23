def getSum(self, a: int, b: int) -> int:
    while b & 255:
        a, b = a ^ b, (a & b) * 2

    return a & 255 if b else a
