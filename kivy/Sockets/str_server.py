# 导入 socket、sys 模块
import socket
import time


HEADERSIZE = 10
# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获取本地主机名，绑定端口号
host=socket.gethostname()
port=1243
s.bind((host, port))
# 设置最大连接数，超过后排队
s.listen(5)

while True:
    # 建立客户端连接
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    msg = "Welcome to the server!"
    msg = f"{len(msg):<{HEADERSIZE}}"+msg
    clientsocket.send(bytes(msg,"utf-8"))

    while True:
        time.sleep(3)
        msg = f"The time is {time.time()}"
        msg = f"{len(msg):<{HEADERSIZE}}"+msg
        print(msg)
        clientsocket.send(bytes(msg,"utf-8"))