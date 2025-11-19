from Crypto.Util.number import long_to_bytes
import math

N = 71265414408164782724799236183731184290483454935475567996082990232753834738522591618102393925219210035328522314373360695452360029719577627759990866649971936124535888856570135200008810318772247262796703223061238662374143334655920441589813687052362510749486735082413500690349387534377197208335977650307181777949
e = 65537
c = 19940010393828927021006982579772211764096780139150134709306565250242961073654540995470785720199848358036764678161244159988392712774059527857798841620117016534366770399280043027665253489263519835038098245129628021622657203912628499548103565647876777005356049009573810952832558629289705804739902477471385578195
H = 1314141272880369748987070958975014964732456047160084498406826910367390908235849010823263035635913130647884562589457527592409825368792501912617286577577052

# --- Tấn công RSA: Phân tích N dựa trên hiệu số H (p - q) ---
# Công thức tìm q: q = (-H + sqrt(H^2 + 4N)) / 2

# 1. Tính delta (biệt thức): Delta = H^2 + 4N
delta = H*H + 4*N

# 2. Tính căn bậc hai nguyên của delta
# math.isqrt() được sử dụng để lấy căn bậc hai nguyên cho số nguyên lớn
sqrt_delta = math.isqrt(delta)

# 3. Kiểm tra tính hợp lệ: đảm bảo delta là một số chính phương
if sqrt_delta * sqrt_delta != delta:
    print("Lỗi: Biệt thức không phải là số chính phương. Gợi ý (hint) có thể không chính xác.")
    exit()

# 4. Tính q sử dụng nghiệm dương của công thức bậc hai: q = (sqrt_delta - H) // 2
q = (sqrt_delta - H) // 2

# 5. Tính p sử dụng p = N / q
p = N // q

# Kiểm tra: Đảm bảo p * q = N
if p * q != N:
    print("Lỗi: p * q không bằng N. Phân tích thừa số thất bại.")
    exit()

# --- Các bước giải mã RSA tiêu chuẩn ---

# 6. Tính hàm phi Euler: phi(N) = (p - 1)(q - 1)
phi_N = (p - 1) * (q - 1)

# 7. Tính khóa riêng d: d = e^-1 mod phi(N)
# d là nghịch đảo modulo của e theo phi_N
# pow(e, -1, phi_N) tính toán nghịch đảo modulo một cách hiệu quả
d = pow(e, -1, phi_N)

# 8. Giải mã c: m = c^d mod N
# Kết quả là flag dưới dạng số nguyên lớn (long integer)
flag_long = pow(c, d, N)

# 9. Chuyển số nguyên lớn về chuỗi byte (định dạng flag ban đầu)
flag = long_to_bytes(flag_long)

# --- In kết quả ---
print("\n--- Kết quả Giải mã RSA ---")
print(f"Thừa số nguyên tố p: {p}")
print(f"Thừa số nguyên tố q: {q}")
print(f"Khóa riêng d: {d}")
print(f"Flag đã giải mã (số nguyên): {flag_long}")
print(f"Flag đã giải mã (bytes): {flag!r}")
try:
    print(f"\nFlag: **{flag.decode('utf-8')}**")
except UnicodeDecodeError:
    print("\nFlag: Không thể giải mã thành chuỗi UTF-8. In dưới dạng byte.")