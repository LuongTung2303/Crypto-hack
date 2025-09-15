from pwn import xor;

cipher_text = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104");
half_plaintext = "crypto{".encode("utf-8");
bytes_0 = bytes(34);
codebreaking_key = half_plaintext + bytes_0 + "}".encode("utf-8");
guess_plaintext = xor(cipher_text, codebreaking_key);
key = "myXORkey00000000000000000y"
print(guess_plaintext);
print(guess_plaintext.decode("utf-8"));