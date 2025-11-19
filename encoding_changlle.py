from pwn import * # pip install pwntools
import json
import base64
import codecs

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def decode_level(receive):
    type = receive["type"];
    encoded = receive["encoded"];
    decoded = "";
    if type == "base64":
        decoded = base64.b64decode(encoded).decode();
    elif type == "hex":
        decoded = bytes.fromhex(encoded).decode();
    elif type == "rot13":
        decoded = codecs.decode(encoded, 'rot_13');
    elif type == "bigint":
        num = int(encoded, 16)
        decoded = num.to_bytes((num.bit_length() + 7) // 8, 'big').decode()
    elif type == "utf-8":
        decoded = "".join([chr(i) for i in encoded]);
    return decoded


for i in range(101):
    received = json_recv() 
    if "flag" in received:
        print("FLAG:", received["flag"])
        break
    to_send = {
        "decoded": decode_level(received)
    }
    json_send(to_send)
