from compress import compression, to_bytes
from decompress import decompress, from_bytes

from encryption_decryption.AESCipher import AESCipher

import socket

aes = AESCipher("EEE3097S")
#text = "what is happening"

#print(aes.encrypt(text))
#print(aes.decrypt(aes.encrypt(text)))

#s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 12345

s.connect(('192.168.137.1', port))
#s.connect(("fe80::d71f:780:ff2:8d7d", port, 0, 21))

while True:
    #decoded_value = s.recv(1024).decode()
    decoded_value = s.recv(2048).decode()
    print(decoded_value)
    decrypted = aes.decrypt(decoded_value)
    #temp = bytearray(decoded_value, 'utf-8')
    print(decrypted)
    #temp = bytearray.fromhex(decrypted)
    temp = bytearray(decrypted)
    print(temp)
    if decoded_value == b'' :
        break
    #if temp == b'':
        #continue
    print( decompress(from_bytes(decrypted)) )


s.close()
