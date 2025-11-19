# Import các thư viện cần thiết
import gmpy2
from Crypto.Util.number import long_to_bytes

N = 156535289744813391484733637004629989693449278011539765430148068036520637521931477118017540221271166255607535061377147373233452980110942455265776213890474965220142368309828275007828001122797315894305578380452056614406844051390135962910369383069032793735593455186950364448092139917100907582123034296711514750767
e = 65537
c = 67507976045834884591599844702776945412520983076543069944605151248585407460146319656228956184490283915611254276785847894805226670523076363415424577267724819689951932435888643361529585004659929585638783382186625532388819006666300133223917976430370089746333159076808050049565697125913056449988850895917763752787

# --- Bước 1: Phân tích N thành thừa số (Factoring N) ---
# Dùng phương pháp phân tích thừa số Fermat vì p và q rất gần nhau.

# Tính căn bậc hai nguyên trên của N. Đây là giá trị khởi điểm cho 'a' (sqrtN)
# command: a = gmpy2.isqrt(N) + 1
a = gmpy2.isqrt(N) + 1

# Bắt đầu vòng lặp để tìm 's' sao cho s^2 = a^2 - N là số chính phương
# command: while not gmpy2.is_square(a**2 - N): a += 1
while not gmpy2.is_square(a**2 - N):
    a += 1

# Tính s (căn bậc hai của a^2 - N)
# command: s = gmpy2.isqrt(a**2 - N)
s = gmpy2.isqrt(a**2 - N)

# Tính p và q
# command: p = a - s
p = int(a - s)
# command: q = a + s
q = int(a + s)

print(f"p = {p}")
print(f"q = {q}")
print(f"Kiểm tra p*q == N: {p*q == N}")

# --- Bước 2: Tính khóa giải mã (Decryption Key 'd') ---

# Tính hàm Euler Totient phi(N) = (p-1)*(q-1)
# command: phi = (p - 1) * (q - 1)
phi = (p - 1) * (q - 1)

# Tính khóa giải mã d = e^-1 mod phi
# command: d = gmpy2.invert(e, phi)
d = gmpy2.invert(e, phi)
d = int(d)

print(f"phi(N) = {phi}")
print(f"d = {d}")

# --- Bước 3: Giải mã bản rõ (Decrypting the message 'm') ---

# Tính m = c^d mod N
# command: m = pow(c, d, N)
m = pow(c, d, N)

# Chuyển bản rõ từ số nguyên về chuỗi byte (flag)
# command: flag = long_to_bytes(m)
flag = long_to_bytes(m)

print("\n--- KẾT QUẢ ---")
print(f"Bản rõ (m) = {m}")
print(f"Flag = {flag.decode()}")