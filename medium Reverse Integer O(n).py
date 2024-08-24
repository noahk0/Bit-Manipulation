def reverse(self, x: int) -> int:
    n = 0

    while x:
        unsign = abs(n)

        if 7 < abs(digit := fmod(x, 10)) and unsign == 214748364 or 214748364 < unsign:
            return 0

        x, n = int(x / 10), n * 10 + digit

    return int(n)
