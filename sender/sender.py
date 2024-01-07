import socket
import os
#print(socket.gethostbyname(socket.gethostname()))
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM )
host=socket.gethostbyname(socket.gethostname())
print(host)
server.bind((host,42069))
server.listen()
client,address=server.accept()
size=os.path.getsize('d:\Download\Flutter Crash Course.mp4')
client.send(str(size).encode())
sent_sum=0
with open('d:\Download\Flutter Crash Course.mp4','rb') as f:
    file=f.read(1024*1024)
    while file!=b'':
        client.send(file)
        sent_sum+=len(file)
        print("%3.1f%s"%(sent_sum*100/size,"%"),sent_sum,end="\r")
        file=f.read(1024*1024)
print("%3.1f%s"%(sent_sum*100/size,"%"),sent_sum)

# import os
# file_walk=os.walk('C:/Users/David/Documents')
# for root,dir,files in file_walk:
#     for x in files:
#         if x.endswith('.jpg') or x.endswith('.png'):
#             print(root,"\ ".strip(),x)
