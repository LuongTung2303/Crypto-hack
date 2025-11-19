from Crypto.Util.number import getPrime, bytes_to_long
from secret import flag


p = getPrime(512)
q = getPrime(512)
N = p * q
e = 65537
assert len(flag) <= 64
flag = bytes_to_long(flag)
c = pow(flag, e, N)
hint = abs(p - q)

print(f"N = {N}\ne = {e}\nc = {c}\nhint = {hint}")