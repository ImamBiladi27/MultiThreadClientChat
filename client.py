import threading
import socket

class Client:
    nama = input(str('masukkan nama'))
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 59000
    client.connect((host, port))
obj=Client()

def clien_menerima():
    while True:
        try:
            message = obj.client.recv(5024).decode('utf-8')
            if message == 'nama?':
                obj.client.send(obj.nama.encode('utf-8'))
            else:
                print(message)
        except:
            print('error')
            obj.client.close()
            break



def client_mengirim():
    while True:

        menginput=input("")
        message = f'{obj.nama}:{menginput}'
        obj.client.send(message.encode())

def THREAD():
    receive_Thread = threading.Thread(target = clien_menerima)
    receive_Thread.start()

    send_Thread = threading.Thread(target=client_mengirim)
    send_Thread.start()

THREAD()