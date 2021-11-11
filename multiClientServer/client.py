import socket

sock = socket.socket()
try:
    sock.connect(('localhost', 8080))

    res = sock.recv(1024)
    while True:
        message = input('Введите сообщение: ')
        sock.send(message.encode())
        res = sock.recv(1024)
        print(res.decode())
    sock.close()

except:
    print('Ошибка соединения')