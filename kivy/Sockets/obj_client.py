import socket
import pickle

HEADERSIZE = 10

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获取本地主机名
host=socket.gethostname()
#设置端口号
port=1243
#连接服务器
s.connect((host, port))

while True:
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(16)# 接收小于 16 字节的数据
        if new_msg:
            print("new msg len:",msg[:HEADERSIZE])
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg

        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg recvd")
            print(full_msg[HEADERSIZE:])

            d=pickle.loads(full_msg[HEADERSIZE:])
            print(d)

            new_msg = True
            full_msg = b""