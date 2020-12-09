import socket
from controller.CarImp.RealCar import RealCar
from controller.CarCameraImp.RealCamera import RealCamera
from time import sleep

def initSocket():
    # create an INET, STREAMing socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # now connect to the web server on port 80 - the normal http port

    while True:
        try:
            print("connecting")
            s.settimeout(3)
            s.connect(("192.168.137.1", 8080))
            s.settimeout(None)
            break
        except KeyboardInterrupt:
            return -1
        except:
            pass

    return s

car = RealCar(RealCamera())
s = initSocket()

while True:
    try:
        receivedBytes = s.recv(2) 

        if receivedBytes:
            receivedBytes = receivedBytes.decode("ascii")
            print(receivedBytes)
            
            if receivedBytes[0] == "C":
                img = car.get_image_from_camera()
                img = img.reshape(16*16)
                msg = img.tobytes()
                s.send(msg)
                
            if receivedBytes[0] == "F":
                car.set_right_speed(2)
                car.set_left_speed(2)
                sleep(0.1)
                car.set_right_speed(0)
                car.set_left_speed(0)

            if receivedBytes[0] == "L":
                speed=int(receivedBytes[1])
                
                car.set_left_speed(speed)
                sleep(0.1)
                car.set_left_speed(0)

            if receivedBytes[0] == "R":
                speed=int(receivedBytes[1])
                car.set_right_speed(speed)
                sleep(0.1)
                car.set_right_speed(0)
                
            if receivedBytes[0] == "S":
                car.set_left_speed(0)
                car.set_right_speed(0)

        else:
            raise Exception()

    except KeyboardInterrupt:
        break
    except:
        print("closing")
        s.close()
        s = initSocket()
        if s == -1:
            break