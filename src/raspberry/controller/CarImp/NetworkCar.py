from ..Car import Car
import socket
import numpy as np

class NetworkCar(Car):
    def __init__(self, carCamera=None, myIp="192.168.137.1", port=8080):
        super().__init__(carCamera)

        # create an INET, STREAMing socket
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # bind the socket to a public host, and a well-known port
        serversocket.bind((myIp, port))
        # become a server socket
        print("listening...")
        serversocket.listen(5)

        (self.clientsocket, address) = serversocket.accept()
        print("{} entered the chat".format(address))

    def set_right_speed(self, speed):
        self.clientsocket.send("R{}".format(int(speed)).encode("ascii"))
    
    def set_left_speed(self, speed):
        self.clientsocket.send("L{}".format(int(speed)).encode("ascii"))

    def get_image_from_camera(self):
        self.clientsocket.send("C0".encode("ascii"))
        return np.frombuffer(self.clientsocket.recv(1000), dtype="uint8").reshape(16, 16)

    def close(self):
        self.clientsocket.close()