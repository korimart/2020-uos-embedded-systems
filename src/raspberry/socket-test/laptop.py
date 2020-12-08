from ..controller.CarImp.NetworkCar import NetworkCar

car = NetworkCar()

while True:
    command = input("command: ")

    if command == "R":
        car.set_right_speed(2)

    if command == "C":
        img = car.get_image_from_camera()
        print(img)