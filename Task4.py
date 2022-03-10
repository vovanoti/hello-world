import os

print("PID: ",os.getpid())
print("It was ran by ",os.getlogin())
print("To work hapily on ",os.uname().sysname,"-",os.uname().release)
