import socket

sock = socket.socket()
sock.setblocking(1)
msg = ""

try:
    sock.connect(('localhost', 8080))
    print('Подключение к серверу успешно')
    while msg != "exit":
        msg = input('Напишите ваше сообщение: ')
        sock.send(msg.encode())
        data = sock.recv(1024)
except:
    print('Ошибка соединения. Остановка...')

sock.close()
