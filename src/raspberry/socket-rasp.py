import socket
from controller.CarImp.RealCar import RealCar
from controller.CarCameraImp.RealCamera import RealCamera

car = RealCar(RealCamera())

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
s.connect(("192.168.137.1", 8080))

while True:
    
    receivedBytes = s.recv(100) 
    if receivedBytes :
        print(receivedBytes)
        
        if receivedBytes == b"C":
            img = car.get_image_from_camera()
            img = img.reshape(16*16)
            msg = img.tobytes()
            s.send(msg)
            
        
        if receivedBytes == b"F":
            car.set_right_speed(2)
            car.set_left_speed(2)

        if receivedBytes == b"L":
            car.set_right_speed(2)

        if receivedBytes == b"R":
            car.set_right_speed(2)
            
        if receivedBytes == b"S":
            car.set_left_speed(0)
            car.set_right_speed(0)
