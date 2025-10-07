def extended_gcd(a, b):
        # base case
    if b == 0:
        # gcd(a,0) = |a|. We choose g = abs(a) and x = sign(a), y = 0
        # but simpler: return (abs(a), 1 if a>=0 else -1, 0) would make ax+by = g.
        # Many implementations return (a, 1, 0) which works as long as caller understands sign.
        return (abs(a), 1 if a >= 0 else -1, 0)

    # recursive step: compute gcd(b, a % b)
    g, x1, y1 = extended_gcd(b, a % b)

    # update coefficients: x = y1, y = x1 - (a // b) * y1
    x = y1
    y = x1 - (a // b) * y1

    return (g, x, y)
    

print((58632*58632)%65537);