from main import main
from ctypes import CDLL
from sys import exit, argv


if __name__ == '__main__':

    #if  == 0_LIBC.ptrace(PTRACE_GETREGS, 0, 0, 0):
    _call = main("127.0.0.1", int(argv[1]), False)
    _call.main()
    del(_call)    
    #else:
    #    print("buen intento :v")
    #    exit(1)