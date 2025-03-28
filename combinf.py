from math import comb

def combinf(n, r, broj):
    if n < r:
        return "n mora biti veće ili jednako r"
    
    ukupno = comb(n, r)
    if broj <= 0 or broj > ukupno:
        return "Broj je izvan raspona"

    kombinacija = []
    broja = broj
    x = 0
    ck = []

    for i in range(1, r + 1):
        ck.append(i)

    for x in range(r):
        for val in range(ck[x] if x > 0 else 1, n + 1):
            f = comb(n - val, r - (x + 1))
            if broja > f:
                broja -= f
            else:
                kombinacija.append(val)
                if x + 1 < r:
                    ck[x + 1] = val + 1
                break

    return kombinacija
