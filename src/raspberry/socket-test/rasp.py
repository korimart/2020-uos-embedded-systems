import socket
from ..controller.CarImp.RealCar import RealCar
from ..controller.CarCameraImp import RealCamera
from ..controller.ControllerImp.KeyboadController import KeyboardController

car = RealCar(RealCamera())
controller = KeyboardController(car)

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
s.connect(("192.168.137.1", 8080))
receivedBytes = s.recv(100)

if receivedBytes == b"goStraight":
    controller.goStraight()
    