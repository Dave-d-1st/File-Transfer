import socket
import time 
t1=time.perf_counter()
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM )
client.connect(('192.168.0.109',42069))
file_size=int(client.recv(1024).decode())
print(file_size)
file=client.recv(file_size)
with open('movie.mkv','wb') as f:
    f.write(file)
t2=time.perf_counter()
print(t2-t1)