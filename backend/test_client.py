import socket
import time


test_message_create_party = '{"endpoint" : "create-party" }'

class Client():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.is_connected = False
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        self.is_connected = True

        # once connected send create party command
        self.socket.send(test_message_create_party.encode())
        self.ping_num = 0 

    def run(self):
        while True:
            time.sleep(1)
            self.socket.send('{"endpoint": "test"}'.encode())
            self.ping_num += 1

client = Client('192.168.0.109', 3000)
client.run()