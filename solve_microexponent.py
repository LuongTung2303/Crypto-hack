import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

a = 1
b = 7
p = 81663996540811672901764249733343363790991183353803305739092974199965546219729
G_coords = (14023374736200111073976017545954000619736741127496973904317708826835398305431, 23173384182409394365116200040829680541979866476670477159886520495530923549144)
P_coords = (63698676086974127123544556591037049117285370657094973402459055228534678256540, 50054613692038253008132268195064761802561717815733137655094406841864102707369)
ciphertext = bytes.fromhex('701d3fed9cf7f5182f2e924ed9f9d23a9a0bf21ac6bf877bb53f6ceb27ae86551df3f27d8820c4bd2552f4953406ba18')
iv = bytes.fromhex('8d79f0db12f8d54f2fd70d067340124f')

### 2. Tạo lại đường cong E và các điểm
E = EllipticCurve(GF(p), [a, b])
G = E(G_coords)
P = E(P_coords)

print(f"[*] Đường cong E: {E}")
print(f"[*] Đang tìm 'x' sao cho P = x*G ...")

### 3. Tìm 'x' (private key)
# 'x' chỉ có 64-bit, quá nhỏ -> Sage log() được
# Đây là lệnh mấu chốt:
x = G.log(P)

print(f"[+] Tìm được x = {x}")

### 4. Từ 'x' tính ra key AES (làm y chang đề)
sha1 = hashlib.sha1()
sha1.update(str(x).encode('ascii'))
key = sha1.digest()[:16] # Lấy 16 byte đầu

print(f"[+] Key AES (hex): {key.hex()}")

### 5. Giải mã tìm flag
cipher = AES.new(key, AES.MODE_CBC, iv)
padded_flag = cipher.decrypt(ciphertext)

# Gỡ padding
flag = unpad(padded_flag, 16)

print("\n=====================")
print(f"FLAG: {flag.decode('utf-8')}")
print("=====================")