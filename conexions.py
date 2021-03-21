from socket import socket
from time import sleep
import pdb
from os import urandom
from sys import exit
from string import ascii_letters, digits
from random import sample
from base64 import b32decode, b32encode
from Crypto.Cipher import AES

def connect(RHOST, RPORT):

    class _Connect:

        def __init__(self, RHOST, RPORT):

            self._CONNECT = socket()
            self._RHOST = RHOST
            self._RPORT = RPORT                

            

        class Encript:

            def __init__(self):
                self.key = b32encode(b"1213123213321313") # clave random de 16 caracteres

            def encrypt(self, data):
                data = b32encode(data)
                cipher = AES.new(b32decode(self.key), AES.MODE_EAX)
                ciphertext, tag = cipher.encrypt_and_digest(data)
                #pdb.set_trace()
                return cipher.nonce + tag + ciphertext

            def decrypt(self, data):
                nonce = data[:AES.block_size]
                tag = data[AES.block_size:AES.block_size * 2]
                ciphertext = data[AES.block_size * 2:]
                cipher = AES.new(b32decode(self.key), AES.MODE_EAX, nonce)
                #pdb.set_trace()
                if len(ciphertext) == 0 and len(tag) == 0:
                    return data
                else:
                    data = cipher.decrypt_and_verify(ciphertext, tag)
                    return b32decode(data).decode()

        def _returnEncript(self):
            Encript = self.Encript()

        def _Send(self, data, encript, client=0):
            if encript == False:
                self._CONNECT.send(data.encode())
            elif encript == True:                
                
                #pdb.set_trace()
                Encript = self.Encript()
                data = data.encode()
                #pdb.set_trace()
                data = Encript.encrypt(data)
                
                #pdb.set_trace()
                buffer_size = len(data)
                buffer_size = str(buffer_size)
                sleep(0.2)
                self._CONNECT.send(buffer_size.encode())
                #pdb.set_trace()
                sleep(0.2)
                self._CONNECT.send(data)
            else:
                self._Close()
                raise TypeError()
        
        def _Recv(self, buffer, descript):
            if descript == False:
                data = self._CONNECT.recv(int(buffer)).decode()
                return data
            elif descript == True:

                #pdb.set_trace()
                
                try:
                    buffer = self._CONNECT.recv(buffer);
                    buffer = int(buffer)
                except (ValueError, TypeError):
                    return buffer
                self._CONNECT.settimeout(None)
                sleep(0.1)
                data = self._CONNECT.recv(int(buffer))
                try:
                    data = int(data)
                except ValueError:
                    Encript = self.Encript()
                    data = Encript.decrypt(data)
                try:
                    return data.decode()
                except AttributeError:
                    return data

            else:
                self._Close()
                raise TypeError()
        
        def _Connect(self):
            while True:
                try:

                    self._CONNECT.connect((self._RHOST, self._RPORT))
                    break

                except ConnectionRefusedError:
                    sleep(1)

        def _CLEAR(self):
            del(self)


        def _Close(self, _exit=True):
            self._CONNECT.close()
            self._CLEAR()
            if _exit == True:
                exit()


    
    return _Connect(RHOST, RPORT)

if __name__ == "__main__":
    print("buen intento")
    exit()