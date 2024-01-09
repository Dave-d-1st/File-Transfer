import socket
import os
import time 
t1=time.perf_counter()
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM )
client.connect(('192.168.43.102',42069))
file_size=int(client.recv(1024).decode())
print(file_size)
size=os.path.getsize('movie.mkv')
file=client.recv(1024*1024)
with open('movie.mkv','wb') as f:
	f.write(file)
print(size)
with open('movie.mkv','ab') as f:
	while size!=file_size:
		file=client.recv(1024*1024)
		f.write(file)
		print("%3.1f%s"%(size*100/(file_size),"%"),size,'\r',end="")
		size=os.path.getsize('movie.mkv')
print("%3.1f%s"%(size*100/(file_size),"%"),size)
t2=time.perf_counter()
print(t2-t1)