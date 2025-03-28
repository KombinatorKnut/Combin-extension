from math import comb

def combino(n, r, nizk):
    if n < r:
        return 0  # Greška: n mora biti >= r

    # Parsiranje kombinacije iz stringa u listu brojeva
    ck = list(map(int, nizk.split()))

    # RBK (redni broj kombinacije) počinje od 1
    RBK = 1

    for b in range(1, r + 1):
        f = comb(n - ck[b - 2], r - b + 1) if b > 1 else comb(n, r - b + 1)
        f1 = comb(n - ck[b - 1] + 1, r - b + 1)
        RBK += f - f1

    return RBK
