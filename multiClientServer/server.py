import socket
from _thread import *


sock = socket.socket()
print('Запуск сервера...')
try:
    sock.bind(('127.0.0.1', 8080))
    print('Успешно')
    sock.listen()


    def connection_thread(conn, addr):
        conn.send(str.encode('Сервер работает:'))
        while True:
            data = conn.recv(1024).decode()
            response = f"Сообщение '{data}' успешно доставлено"
            print(f"{addr}: {data}")
            if not data:
                break
            conn.sendall(response.encode())
        conn.close()


    while True:
        conn, addr = sock.accept()
        print('Новый клиент: ' + addr[0] + ':' + str(addr[1]))
        start_new_thread(connection_thread, (conn, addr))
    sock.close()
except:
    print('Ошибка. Остановка сервера...')
