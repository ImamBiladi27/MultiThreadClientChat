import socket
import threading

class Server:
    host = socket.gethostname()
    port = 59000

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    clients = []
    nama = []
obj=Server()

def siaran(message, currentClient):
    file2 = open("data/riwayat.txt", "a")
    file2.write(str(message) + "\n")
    for client in obj.clients:
       if(client != currentClient):
           client.send(message)
    file2.close()

def mengurus_client(client):
    while True:
        try:

            message = client.recv(5024)
            siaran(message, client)
            print(message)

        except:

            index = obj.clients.index(client)
            obj.clients.remove(client)
            client.close()

            alias = obj.nama[index]
            keluar= (f'{alias} telah meninggalkan chat'.encode())
            siaran(keluar, 0)
            obj.nama.remove(alias)
            break

def menerima():
    while True:
        print('Server telah dimulai dan berjalan')
        client, address = obj.server.accept()
        print('tersambung dengan: '+str(address))
        client.send('nama?'.encode())
        isi_nama = client.recv(1024)
        obj.nama.append(isi_nama)
        obj.clients.append(client)


        message = (f'{isi_nama} telah terhubung'.encode())
        print(message)
        siaran(f'{isi_nama} telah terhubung ke chat room'.encode(),0)

        thread = threading.Thread(target = mengurus_client, args=(client, ))
        thread.start()

menerima()