import socket

for port in range(1, 100):
    try:
        s = socket.socket()
        s.connect(("xxx.xxx.xxx.xxx", port))
        print("[+]Port", port)
        print(s.recv(1024))
        socket.close()
        print("=" + 10)
    except:
        pass
