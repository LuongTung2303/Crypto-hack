from pwn import xor;
from string import ascii_lowercase, ascii_uppercase, digits

cipher_text = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104");
half_plaintext = "crypto{1".encode("utf-8");
bytes_0 = bytes(32);
codebreaking_key = half_plaintext + bytes_0 + "}".encode("utf-8");
guess_plaintext = xor(cipher_text, codebreaking_key);
print(guess_plaintext);
key = "myXORkey"
key_bytes = key.encode("utf-8");
plaintext2 = xor(cipher_text, key_bytes);
print(plaintext2);


